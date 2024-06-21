# qsreplace

`qsreplace` is a Python utility to replace query parameters in URLs.

## Installation

You can install `qsreplace` using pip:

```bash
pip3 install qsreplace
```

## Usage

After installing `qsreplace`, you can use it in your Python scripts. Here's how you can use the `qsreplace` function:

```python
from qsreplace import qsreplace

# Example usage
hosts_file = "example_hosts.txt"
payloads = ["new_value", "another_value"]

replaced_urls = qsreplace.qsreplace(hosts_file, payloads, edit_base_url=True)

for url in replaced_urls:
    print(url)
```

In the example above:
- `example_hosts.txt` should contain a list of URLs, each on a new line.
- `payloads` is a list of values that will replace query parameters in the URLs read from `hosts_file`.
- `edit_base_url` tells qsreplace whether or not to append payload to base urls i.e. which doesn't contain any parameters in it.
- The function `qsreplace.qsreplace` processes each URL, replacing query parameters with each payload in `payloads`.
