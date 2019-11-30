# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
# then tell them whether they guessed too low, too high, or exactly right
# Extras: 
#   1. Keep the game going until the user types “exit”
#   2. Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

number = random.randint(1,50)
count = 0 # number of guesses

while True:
  typed = input('Guess the number[1-50] (type exit to finish the game): ')
  
  if typed.upper() == 'EXIT':
    break

  count += 1
  guess = int(typed)
  
  if guess < number:
    print('Too low')
  elif guess > number:
    print('Too high')
  else:
    print('Congrats. You got it right!')
    print(f'You have made {count} guesses')
    break



