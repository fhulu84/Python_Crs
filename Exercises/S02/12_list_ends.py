# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

def get_list_ends(li):
  return li[:1] + li[-1:]

a = [5, 10, 15, 20, 25]

print(get_list_ends(a))
