# Prettify JSON

This script searches file _raw.json_ in current working directory and output it's content to the terminal in human readable format.

You can specify input file with parameter -f or --file

# Quickstart

To run this script, you need any file with valid json content.
example.json content:
```
{"hello":"world", "value":13}
```

Example of script launch on Linux, Python 3.5:

```bash

$ python3 pprint_json.py -f example.json 
{
    "hello": "world",
    "value": 13
}


```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
