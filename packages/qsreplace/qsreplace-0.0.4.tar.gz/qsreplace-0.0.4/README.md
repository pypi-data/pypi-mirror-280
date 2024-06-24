# qsreplace

`qsreplace` is a Python utility to replace query parameters in URLs.

## Installation

You can install `qsreplace` using pip:

```bash
pip install qsreplace
```

## Usage

After installing `qsreplace`, you can use it in your Python scripts. Here's how you can use the `qsreplace` function:

```python
from qsreplace import qsreplace

# Example usage
url_lst = ["https://example.com", "https://example.com/?param=value"]
payloads = ["new_value", "another_value"]

replaced_urls = qsreplace(url_lst, payloads, edit_base_url=True)

for url in replaced_urls:
    print(url)
```

Result:

```
https://example.com/new_value
https://example.com/another_value
https://example.com/?param=new_value
https://example.com/?param=another_value
```

In the example above:
- `url_lst` should contain a list of URLs
- `payloads` is a list of values that will replace query parameters in the URLs List
- `edit_base_url` tells qsreplace whether or not to append payload to base urls i.e. which doesn't contain any parameters in it.


