# Create a program that asks the user to enter their name and their age. Print out a message addressed to them
# that tells them the year that they will turn 100 years old.

import datetime

name = input('Your name: ')
age = int(input('Your age: '))

print(f'You will turn 100 years old in {100 - age + datetime.datetime.now().year}')
