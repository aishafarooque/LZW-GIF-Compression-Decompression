pip install tabulate

rm -rf data.lzw

mkdir huffman
mkdir huffman/ASCII
mkdir huffman/ABC
mkdir huffman/uppercase

python3 huffman/huffman.py -i uppercase -s small
