# arrange String characters such that lowercase letters should come first

def lowercase_first(str):
  lowers = ''
  uppers = ''
  for c in str:
    if c.islower():
      lowers += c
    else:
      uppers += c
  
  return lowers + uppers


input_str = input('Enter a string containing lowercase and uppercase letters: ')
print('Arranging characters giving precedence to lowercase letters:')
print(lowercase_first(input_str))