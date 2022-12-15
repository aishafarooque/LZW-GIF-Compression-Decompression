from collections import Counter
import random
import os
from tabulate import tabulate
import string
import argparse

class Compress:
    def __init__(self, inputFileName, outputFileName):
        self.inputFileName = inputFileName
        self.outputFileName = outputFileName

        self.dictionary = {}
        self.dictionarySize = -1

        self.compressedIntegerCodes = []

    def build_dictionary_with_character_key(self):
        for i in range(0, 256):
            characterASCII = chr(i)
            self.dictionary[characterASCII] = i

    def compress(self, BYTE_SIZE, BYTE_ORDER):

        self.build_dictionary_with_character_key()
        rawInputFile = open(self.inputFileName)
        compressedOutputFile = open(self.outputFileName, 'wb')
        imageData = rawInputFile.read()

        previousString = ''
        nextDictionaryIndex = 257

        for i, character in enumerate(imageData):

            currentString = previousString + character

            if currentString not in self.dictionary:
                self.dictionary[currentString] = nextDictionaryIndex
                nextDictionaryIndex += 1

                # Packing bits will save space.
                compressedPixel = int(self.dictionary[previousString])
                data = compressedPixel.to_bytes(BYTE_SIZE, byteorder=BYTE_ORDER)
                compressedOutputFile.write(data)
                previousString = currentString[-1]

            else:
                previousString += character

            if i == len(imageData) - 1:
                if previousString in self.dictionary:
                    compressedPixel = int(self.dictionary[previousString])
                    data = compressedPixel.to_bytes(BYTE_SIZE, byteorder=BYTE_ORDER)
                    compressedOutputFile.write(data)

        # This size will be used in the decompression for-loop
        # to construct the dictionary.
        self.dictionarySize = nextDictionaryIndex

        rawInputFile.close()
        compressedOutputFile.close()

        # Delete dictionary to save RAM.
        del self.dictionary

        sizeAfterCompression = os.path.getsize(self.outputFileName)

        return sizeAfterCompression

class Tree:
    def __init__(self, left, right):
        self.left       = left
        self.right      = right

def getCodes(node, path=''):
    """Returns 0/1 codes (dictionary) for the tree starting at root."""

    codes = {}

    try:
        left, right = node.left, node.right
        if left: codes.update(getCodes(left, path + '0'))
        if right: codes.update(getCodes(right, path + '1'))
        if not left and not right: codes[node] = path
    except AttributeError:
        codes = { node: path }

    return codes

def tree(nodes):
    """ Find the two smallest nodes, contracts them, and
    adds to the tree. """

    # Sorting reversed because we want to find the smallest
    # nodes first and contract them.
    nodes = sorted(frequencies.items(), reverse=True)

    # Since we're contracting two edges at a time,
    # we need to make sure there's always one node left in the
    # array.
    while len(nodes) > 1:

        # Find the two smallest nodes.
        left, leftFrequency = nodes[0]
        right, rightFrequency = nodes[1]

        cumulativeFrequency = leftFrequency + rightFrequency

        # Remove them from the array.
        nodes.remove((left, leftFrequency))
        nodes.remove((right, rightFrequency))

        # Contract and add new node to the tree.
        nodes.append((Tree(left, right), cumulativeFrequency))

        # Sort nodes according to their cumulative frequency
        nodes = sorted(nodes, key=lambda tup: tup[1])

    return getCodes(nodes[0][0])

def space(frequencies, originalString):
    spaceBefore, spaceAfter = 0, 0

    spaceBefore = len(originalString) * 8

    # Calculate the message size, defined as
    # size = frequency * code.length()
    for node in huffmanTree:
        frequency = frequencies[node]           # int
        spaceAfter += frequency * len(huffmanTree[node])
    return spaceBefore, spaceAfter

def generateRandomCharacterString(fileName, stringSize, outputType):
    result = ''
    for _ in range(stringSize):

        if outputType == 'ASCII': character = random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
        elif outputType == 'ABC': character = random.choice(['A', 'B', 'C'])
        elif outputType.lower() == 'uppercase': character = random.choice(string.ascii_uppercase)

        result += character

    with open(fileName, 'w') as f:
        f.write(result)
    f.close()

def makeDirectory(name):
    try:
        os.mkdir(INPUT_FILE_PREFIX + '/' + name)
    except:
        pass

if __name__ == '__main__':

    INPUT_FILE_PREFIX = 'huffman'
    COMPRESSED_NAME = 'huffman/data.lzw'

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--Input", help = "Data Type, ASCII or ABC")
    parser.add_argument("-s", "--Size", help = "Data Size, small or big")
    args = parser.parse_args()

    if args.Input == 'ASCII': inputType = 'ASCII'
    elif args.Input == 'ABC': inputType = 'ABC'
    elif args.Input == 'uppercase': inputType = 'uppercase'
    else:
        print ('Unidentified input type. Enter ABC or ASCII.')
        exit(0)

    if args.Size == 'small': stringSizes = [30, 100, 2000, 30000, 50000]
    elif args.Size == 'big': stringSizes = [100000, 500000, 1000000, 5000000, 10000000]
    else:
        print ('Unidentified input size. Enter small or big.')
        exit(0)

    tableHeaders = ['String Length', 'String Size', 'LZW Compression Size', 'Huffman Compression Size']
    tableRows = []

    for size in stringSizes:
        print (f'Starting {size}')
        if size > 100000:
            BYTE_SIZE = 8
            BYTE_ORDER = 'big'
        else:
            BYTE_SIZE = 2
            BYTE_ORDER = 'little'

        inputFileName = INPUT_FILE_PREFIX + '/' + inputType + '/data_' + str(size) + '.txt'

        if not os.path.exists(inputFileName):
            makeDirectory(inputType)
            generateRandomCharacterString(inputFileName, size, inputType)
            print (f'Generated {size} characters')

        file = open(inputFileName)
        alphabets = file.read()

        # Huffman
        frequencies = dict(Counter(alphabets))

        huffmanTree = tree(frequencies)
        stringSize, huffmanSize = space(frequencies, alphabets)
        print (f'Finished Huffman')

        compress = Compress(inputFileName, COMPRESSED_NAME)
        lzwSize = compress.compress(BYTE_SIZE, BYTE_ORDER)
        print (f'Finished LZW')

        tableRows.append([len(alphabets), size, lzwSize, huffmanSize])
        print (f'Finished {size}\n')

    print(tabulate(tableRows, headers=tableHeaders))
