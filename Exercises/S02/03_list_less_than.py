# Take a list and write a program that prints out all the elements of the list that are less than 5.
# Extras:
#   1. Instead of printing the elements one by one, make a new list 
#   that has all the elements less than 5 from this list in it and print out this new list.
#   2. Write this in one line of Python
#   3. Ask the user for a number and return a list that contains only elements from the original list a 
#   that are smaller than that number given by the user.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Take a list...
for n in numbers:
  if n < 5:
    print(n)

# Extras: 1 & 2 & 3
num = int(input('Enter a number: '))

print(list(filter(lambda n: n < num, numbers)))   # Solution 1

print([n for n in numbers if n < num])            # Solution 2, list comprehension
