# Given a string of odd length greater 7, return a string made of the middle three chars of a given String

def get_middle_three_chars(str):
  if len(str) < 7 or len(str) % 2 == 0:
    raise ValueError
  start = int(len(str) / 2) - 1
  return str[start:start+3]

while True:
  try:
    my_str = input('Enter a string: ')

    print(f'\nOriginal string is {my_str}')
    print(f'Middle three chars: {get_middle_three_chars(my_str)}')
    break
  except ValueError:
    print('String length has to be greater than 7 and odd number')