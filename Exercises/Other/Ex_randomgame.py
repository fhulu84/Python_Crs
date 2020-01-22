'''
run: Ex_randomgame.py start end
'''
from random import randint
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

target = randint(start, end)

while True:
  try:
    guess = int(input(f'Write a number between {start}-{end}: '))
    if guess == -1: #ESC
      break
    
    if guess == target:
      print(f'Congratulations. You found the number {target}') 
      break
    elif guess < target:
      print('Higher, try again!')
    elif guess > target:
      print('Lower, try again!')
  except ValueError:
    print('Please enter a number')
  