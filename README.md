# LZW Data Compression and Decompression Algorithm

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-360/)

This repository contains the code for the Lempel-Ziv-Welch Data Compression Algorithm. It has been modified to be applied on compression and decompression a .GIF file.

![](input/the-office.gif)

## Requirements and Libraries
- Python3
- struct: https://docs.python.org/3/library/struct.html


## How to run:

To run this repository, enter the following into your terminal:
```
bash run.sh
```
The file can also be run using the following, but make sure to delete the output folder:
```
python3 main.py
```

The run file will sanitize the working directory to remove any old outputs. It will make the `output/` and `results/` folder. And then, run a command to launch the `main.py` file.

## File Structure

- The `input/` folder contains the .gif file to be processed. Only one file can be processed at a time.
- The `output/` folder contains intermediate files created during compression and decompression.
    - `encoded_gif.txt` is the .gif file as a string
    - `lzw-compressed.lzw` is the output after compressing.
    - `lzw-decompressed.txt` is the output after decompressing.
- The `report/` folder contains the pseudocode for the compression and decompression algorithms.
- `processGif.py` contains the code to convert the gif file to and from a string.

## References
All references for the code have been left above or below it. The LZW algorithm is based on the textbooks:
- Information And Entropy, Chapter 3.7.1 - LZW Example 1 and 2 (Paul Penfield, Jr.)
- Data Structures & Their Algorithms, Harper Collins Publishers, Harry R. Lewis and Larry Denenberg, 1991, and Data Structures and Algorithms, A. Drozdek, Brooks/Cole 2001.
- Cover, T. M., Thomas, J. A. (2006). Elements of Information Theory 2nd Edition (Wiley Series in Telecommunications and Signal Processing). Wiley-Interscience
