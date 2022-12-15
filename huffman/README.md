# Huffman vs. LZW Comparison
[![GitHub forks](https://img.shields.io/github/forks/Naereen/StrapDown.js.svg?style=social&label=Repository&maxAge=2592000)](https://github.com/aishafarooque/LZW-GIF-Compression-Decompression)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-360/)

This repository contains `huffman.py` which contains the code to run LZW and Huffman.py on inputs between [30, 10000000].

This code can also be found at https://github.com/aishafarooque/LZW-GIF-Compression-Decompression.

## Table of Contents
1. [Requirements and Libraries](#requirements)
2. [How to run](#howtorun)
3. [Argument Parse Supported Parameters](#argparser)
4. [File Structure](#filestructure)
5. [Expected Output](#expected)


## Requirements and Libraries<a name="requirements"></a>
- Python3
- tabulate: https://pypi.org/project/tabulate/
- argparse (1.1): https://pypi.org/project/argparse/
- Collections: https://docs.python.org/3/library/collections.html
    - Counter: https://docs.python.org/3/library/collections.html#collections.Counter

## How to run<a name="howtorun"></a>
The code runs using one of the following commands from the `implementation` folder:
```console
aishafarooque@implementation~$ python3 huffman/huffman.py -i ABC -s small
```
This file can also be run using the following. It will install tabulate remove and create new data folders, and run `python3 huffman/huffman.py -i uppercase -s small`:
```console
aishafarooque@implementation~$ bash huffman/huffman.py
```

### Argument Parse Supported Parameters:<a name="argparser"></a>
- `-i` - Input/characters to use in strings, can be:
    - `uppercase`: Generate strings only with uppercase letters [A...Z]
    - `ASCII`: Generate strings using uppercase and lowercase alphabets, or digits
    - `ABC`: Generate strings using only [A,B,C]
- `-s` - Input size/length, can be:
    - `small` - Strings of size, [30, 100, 2000, 30000, 50000]
    - `big` - Strings of size, [100000, 500000, 1000000, 5000000, 10000000]


## File Structure<a name="filestructure"></a>
- `ASCII`, `ABC` and `uppercase` contain the data generate by `huffman.py`.
- `huffman.py` contains LZW, Huffman code and is the driver function.
- `huffman.sh` will remove the data folders, make new folders, and run `huffman.py`.

## Expected Output<a name="expected"></a>
For `python3 huffman/huffman.py -i uppercase -s small`, the expected output is:
```
  String Length    String Size    LZW Compression Size    Huffman Compression Size
---------------  -------------  ----------------------  --------------------------
             30             30                      60                         121
            100            100                     186                         462
           2000           2000                    2552                        9487
          30000          30000                   26936                      142866
          50000          50000                   42232                      238094
```
