#!/bin/python3

from urllib.parse import urlparse, urlencode, parse_qs, urlunparse

def qsreplace(hosts_file, payloads_lst, edit_base_url=True):
    replaced_urls_lst = []
    
    with open(hosts_file, "r") as f:
        url_lst = f.read().splitlines()
        
    for url in url_lst:
        parsed_url = urlparse(url)
        
        if not parsed_url.query:  # If URL doesn't have any query parameters
            if edit_base_url:
                if not url.endswith('/'):
                    url += '/'  # Ensure URL ends with a slash
                for payload in payloads_lst:
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
                        replaced_urls_lst.append(new_url)

    return replaced_urls_lst
