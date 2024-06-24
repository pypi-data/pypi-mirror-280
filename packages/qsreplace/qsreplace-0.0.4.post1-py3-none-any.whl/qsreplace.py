from urllib.parse import urlparse, urlencode, parse_qs, urlunparse
from urllib.parse import quote, unquote

def qsreplace(url_lst, payloads_lst, edit_base_url=True, url_encode=True):
    replaced_urls_lst = []
        
    for url in url_lst:
        parsed_url = urlparse(url)
        
        if not parsed_url.query:  # If URL doesn't have any query parameters
            if edit_base_url:
                if not url.endswith('/'):
                    url += '/'  # Ensure URL ends with a slash
                for payload in payloads_lst:
                    if url_encode:
                        payload = quote(payload)
                    replaced_urls_lst.append(f"{url}{payload}")  # Append payloads directly to the URL
        else:
            query_params = parse_qs(parsed_url.query, keep_blank_values=True)
            
            for param_name, param_values in query_params.items():
                for param_value in param_values:
                    for payload in payloads_lst:
                        new_query_params = query_params.copy()
                        new_query_params[param_name] = payload
                        new_query = urlencode(new_query_params, doseq=True)
                        new_url = urlunparse(parsed_url._replace(query=new_query))
                        if not url_encode:
                            new_url = unquote(new_url)
                        replaced_urls_lst.append(new_url)

    return replaced_urls_lst
