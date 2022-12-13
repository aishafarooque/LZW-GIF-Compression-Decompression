from struct import *
import os

# This implementation is based on the book
#  - Information And Entropy, Chapter 3.7.1 - LZW Example 1 and 2 (Paul Penfield, Jr.)
# -  Data Structures & Their Algorithms, Harper Collins Publishers, Harry R. Lewis and Larry
#    Denenberg, 1991, and Data Structures and Algorithms, A. Drozdek, Brooks/Cole 2001.

class Compress:

  def __init__(self, inputFileName, outputFileName):
    self.inputFileName = inputFileName
    self.outputFileName = outputFileName

    self.dictionary = {}
    self.dictionarySize = -1

    self.compressedIntegerCodes, self.decompressedIntegerCodes = [], []

  def build_dictionary_with_character_key(self):
    """
    Builds dictionary with the character as the key.
    For example, dictionary = {
      'a': 97, 'b': 98, 'c': 99, 'd': 100
    }
    """
    for i in range(0, 256):
      characterASCII = chr(i)
      self.dictionary[characterASCII] = i

  def build_dictionary_with_ASCII_key(self):
    """
    Builds dictionary with the ASCII value as the key.
    For example, dictionary = {
      97: 'a', 98: 'b', 99: 'c', 100: 'd'
    }
    """
    self.dictionary = {}

    for i in range(0, 256):
      characterASCII = chr(i)
      self.dictionary[i] = characterASCII

  def compress(self):

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

        # Convert the strings to bytes using the struct library
        # Reference = https://docs.python.org/3/library/struct.html
        # Packing bits will save space.
        compressedOutputFile.write(
            pack('>H', int(self.dictionary[previousString])))
        previousString = currentString[-1]
      else:
        previousString += character

      if i == len(imageData) - 1:
        if previousString in self.dictionary:
          compressedOutputFile.write(
              pack('>H', int(self.dictionary[previousString])))

    # This size will be used in the decompression for-loop
    # to construct the dictionary.
    self.dictionarySize = nextDictionaryIndex

    rawInputFile.close()
    compressedOutputFile.close()

    # Delete dictionary to save RAM.
    del self.dictionary

  def decompress(self):

    # This will be used to store new codes inside the
    # dictionary.
    nextAvailableDictionaryIndex = 257
    self.build_dictionary_with_ASCII_key()

    compressedOutputFile = open(self.outputFileName, 'rb')
    imageData = []

    for _ in range(self.dictionarySize):
      # Start reading with two bytes at a time because otherwise, we cannot
      # unpack since the required buffer size is 2.
      # Reference - https://www.devdungeon.com/content/working-binary-data-python
      compressedImageData = compressedOutputFile.read(2)
      if len(compressedImageData) != 2:
        break

      # struct.unpack takes bytes and converts them to their 'higher-order' equivalents.
      # Reference - https://stackoverflow.com/a/64362371/7155281
      compressedImageData = unpack('>H', compressedImageData)[0]
      imageData.append(compressedImageData)

    previousCode = None

    for i, integerCode in enumerate(imageData):

      # Special edge case where we're trying to get the integer code
      # for an entry not inside the dictionary.
      if integerCode not in self.dictionary:
        # Update dictionary by appending first character of the string
        # to avoid failure from the edge case.
        self.dictionary[integerCode] = previousCode + previousCode[0]

      if i > 0:
        # Add the next code and it's string to the dictionary
        self.dictionary[
            nextAvailableDictionaryIndex] = previousCode + self.dictionary[
            integerCode][0]
        nextAvailableDictionaryIndex += 1

      previousCode = self.dictionary[integerCode]
      self.decompressedIntegerCodes.append(previousCode)

    with open('output/lzw-decompressed.txt', 'w') as decompressedOutputFile:
      for data in self.decompressedIntegerCodes:
        decompressedOutputFile.write(data)

    decompressedOutputFile.close()

    # Delete dictionary to save RAM.
    del self.dictionary
