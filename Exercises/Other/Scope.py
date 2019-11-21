# Scope- what variables do I have access to?
a = 1

# LOCAL
# def confusion():
#   a = 5
#   return a

# print(confusion()) #5
# print(a)           #1

# PARENT LOCAL
# def parent():
#   a = 10
#   def confusion():
#     return a
#   return confusion()

# print(parent())      #10
# print(a)             #1

# GLOBAL
# def parent():
#     def confusion():
#         return a
#     return confusion()


# print(parent())  # 1
# print(a)  # 1

#BUILT-IN PYTHON FUNCTIONS
# def parent():
#   def confusion():
#     return sum
#   return confusion()

# print(parent())
# print(a)

#GLOBAL KEYWORD
total = 0 

# def count():
#   global total #i am using global total, otherwise gives me an error
#   total += 1 
#   return total

# count()
# count()
# print(count())

#GLOBAL as A PARAMETER
# def count(total):
#   total += 1
#   return total

# count(total)
# count(total)
# print(count(total)) #1

# print(count(count(count(total)))) #3

#NON-LOCAL KEYWORD
# def outer():
#   x = 'local'
#   def inner():
#     nonlocal x
#     x = 'nonlocal'
#     print('inner: ', x)
  
#   inner()
#   print('outer: ', x)

# outer() #inner: nonlocal outer:nonlocal

print("Hello".replace(1,'a'))
cart = ['notebooks']





