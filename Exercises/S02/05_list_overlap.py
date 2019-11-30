# Take two lists and write a program that returns a list that contains only the elements that are common
# between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.
# Ekstras: 
#   1. Randomly generate two lists to test this
#   2. Write this in one line of Python 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(set(a).intersection(set(b)))

# Ekstras
import random

a = [n for n in random.choices(range(1, 50), k=20)]
b = [n for n in random.choices(range(1, 50), k=20)]

print(f'a = {a}')
print(f'b = {b}')

print(set(a).intersection(set(b)))


