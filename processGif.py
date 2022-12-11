import base64

class ProcessGif:

  def __init__(self) -> None:
    pass

  def convert(self, inputFileName, outputFileName):
    with open(inputFileName, 'rb') as gif_file:
      encoded_string = base64.b64encode(gif_file.read())
      gif_file.close()

    with open(outputFileName, 'wb') as encoded_gif:
      encoded_gif.write(encoded_string)
      encoded_gif.close()

    print (f'File encoded and saved to {outputFileName}')

  def deconvert(self, inputFileName, outputFileName):
    with open(inputFileName, 'rb') as lzw_output:
      encoded_string = base64.b64decode(lzw_output.read())
      gifFile = open(outputFileName, 'wb')
      gifFile.write(encoded_string)
      gifFile.close()

      print (f'File decoded and saved to {outputFileName}')
