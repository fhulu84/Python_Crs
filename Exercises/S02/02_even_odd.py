# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. 
# Extras:
  # 1. If the number is a multiple of 4, print out a different message.
  # 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
  # If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


num = int(input('Enter a number: '))
msg = 'Even' if num % 2 == 0 else 'Odd'
print(f'{num} is {msg}.', end='')

if num % 4 == 0:
  print(' It can also be divisible by 4')

check = int(input('Enter a number to divide by: '))
if num % check == 0:
  print(f'{num} is divisible by {check}')
else:
  print(f'{num} is not divisible by {check}')



