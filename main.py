from compress import Compress
from processGif import ProcessGif
import os
import argparse

if __name__ == '__main__':

  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--Input", help = "GIF Name, must be inside input/ folder")
  args = parser.parse_args()


  if args.Input:
    INPUT_GIF_NAME = args.Input
  else:
    print ('Cannot find GIF name. Using the-office.gif')
    inputFolderPrefix = 'input/'
    INPUT_GIF_NAME = inputFolderPrefix + 'the-office.gif'

  outputFolderPrefix = 'output/'
  ENCODED_GIF_NAME = outputFolderPrefix + 'encoded_gif.txt'
  COMPRESSED_NAME = outputFolderPrefix + 'lzw-compressed.lzw'
  DECOMPRESSED_NAME = outputFolderPrefix + 'lzw-decompressed.txt'

  resultFolderPrefix = 'result/'
  OUTPUT_GIF_NAME = resultFolderPrefix + 'lzw-gif.gif'

  processor = ProcessGif()

  # Convert the .gif file to base64 encoding
  encodedFileName = processor.convert(inputFileName=INPUT_GIF_NAME,
                                     outputFileName=ENCODED_GIF_NAME)

  compress = Compress(ENCODED_GIF_NAME, COMPRESSED_NAME)
  compress.compress()
  compress.decompress()

  # Convert the base64 encoding to .gif file
  processor.deconvert(inputFileName=DECOMPRESSED_NAME,
                      outputFileName=OUTPUT_GIF_NAME)

  sizeBeforeCompression = os.path.getsize(INPUT_GIF_NAME)
  sizeAfterCompression = os.path.getsize(OUTPUT_GIF_NAME)

  print (f'Size before compression: {sizeBeforeCompression}')
  print (f'Size after compression: {sizeAfterCompression}')

  if sizeBeforeCompression == sizeAfterCompression:
    print (f'No data was lost after compression and decompression')
  else:
    print (f'Data was lost after compression and decompression')
