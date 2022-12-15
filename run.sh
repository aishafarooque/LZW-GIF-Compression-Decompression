# This file sanitizes the working repository,
# and runs the python file.
rm -rf output/
rm -rf result/

# The output folder will contain intermediate compression
# and decompression files.
mkdir output

# The result folder will contain the decompressed GIF.
mkdir result

python3 main.py -i input/the-office.gif
