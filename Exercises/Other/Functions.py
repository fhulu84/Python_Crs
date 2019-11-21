# def say_hello(name = 'Mate', emoji=':)'):
#   print(f'Helloo {name}{emoji}')

# say_hello('Hilal',':p')
# say_hello()

# def sum(num1, num2):
#   return num1 + num2

# print(sum(4,5))
# print(sum(sum(10,20),10))

# def is_even(num):
#   return num % 2 == 0

# print(is_even(5))
# print(is_even(2))

# *ARGS & **KWARGS
def super_func(*args, **kwargs):
  total = 0
  for item in kwargs.values():
    total += item
  return sum(args) + total

# super_func(1,2,3,4,5) #without **kwargs
print(super_func(1,2,3,4,5, num1=5, num2=10))
