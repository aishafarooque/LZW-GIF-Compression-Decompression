from compress import Compress
from processGif import ProcessGif

if __name__ == '__main__':

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
