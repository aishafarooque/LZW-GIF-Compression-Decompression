# Huffman vs. LZW Comparison

This repository contains `huffman.py` which contains the code to run LZW and Huffman.py on inputs between [30, 10000000].

## Requirements and Libraries
- Python3
- tabulate: https://pypi.org/project/tabulate/
- argparse (1.1): https://pypi.org/project/argparse/
- Collections: https://docs.python.org/3/library/collections.html

    - Counter: https://docs.python.org/3/library/collections.html#collections.Counter

## How to run:
The code runs using one of the following commands from the `implementation` folder:
```console
aishafarooque@implementation~$ python3 huffman/huffman.py -i ABC -s small
```

### Argument Parse Supported Parameters:
- `-i` - Input/characters to use in strings, can be:
    - `uppercase`: Generate strings only with uppercase letters [A...Z]
    - `ASCII`: Generate strings using uppercase and lowercase alphabets, or digits
    - `ABC`: Generate strings using only [A,B,C]
- `-s` - Input size/length, can be:
    - `small` - Strings of size, [30, 100, 2000, 30000, 50000]
    - `big` - Strings of size, [100000, 500000, 1000000, 5000000, 10000000]
