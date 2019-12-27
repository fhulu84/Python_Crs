# GoogleTrans API solution
# It is online
# from googletrans import Translator

# with open('test.txt', 'r') as f:
#   content = f.read()

# translator = Translator()

# print(translator.translate(content, dest='es').text)

# OFFLINE translator solution
from translate import Translator

try:
  with open('./test.txt', mode='r') as f:
    content = f.read()
  translator = Translator(to_lang='es')
  print(translator.translate(content))
except FileNotFoundError as e:
  print('File not found')
