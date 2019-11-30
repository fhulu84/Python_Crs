# Given a string input Count all lower case, upper case, digits, and special symbols

def count_char_types(str):
  chars = 0
  digits = 0
  symbols = 0

  for c in str:
    if c.isalpha():
      chars += 1
    elif c.isnumeric():
      digits += 1
    else:
      symbols += 1

  print(f'"{str}" consists of {chars} chars, {digits} digits and {symbols} symbols')


input_str = input('Enter a string consisting of different char types: ')
print()
count_char_types(input_str)