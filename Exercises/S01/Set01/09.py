# Reverse a given number and return true if it is the same as the original number

def is_reversed_same(num):
  reverse = num[::-1]
  return reverse == num

num = input('Enter a number: ')
print(f'Is original and reverse equal : {is_reversed_same(num)}')