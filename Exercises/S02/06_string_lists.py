# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

str = input('Enter a string: ')

if str.upper() == str[::-1].upper():
  print(f'{str} is a palindrome')
else:
  print(f'{str} is not a palindrome')