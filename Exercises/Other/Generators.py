# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result

# my_list = make_list(1000000) #this takes a lot of memory, we dont want to use them in memeory to be able to use it
# print(my_list)


# def generator_function(num):
#     for i in range(num):
#         # yield i            # pauses function until come back
#         yield i*2

# # for item in generator_function(100):
# #   print(item)


# g = generator_function(100)
# print(next(g))  # we can call next until the range is valid
# print(next(g))
# print(next(g))

# GENERATORS PERFORMANCE (Updated version of decorators performance)
# from time import time

# def performance(fn):
#   def wrapper(*args, **kwargs):
#     t1 = time()
#     result = fn(*args, **kwargs)
#     t2 = time()
#     print(f'took {t2-t1} s')
#     return result
#   return wrapper

# @performance
# def long_time():
#   print('1')
#   for i in range(10000000):
#     i*5

# @performance
# def long_time2():
#   print('2')
#   for i in list(range(10000000)):
#     i*5

# long_time()   # this one is faster, but not a big difference as in repl.it
# long_time2()

# def gen_fun():
#   for i in range(50):
#     yield i

# for item in gen_fun():
#   print(item) 

# OUR OWN FOR LOOP, for loops work like this under the hood
# def special_for(iterable):
#   iterator = iter(iterable) # iter gives us the opportunity to use next()
#   while True:
#     try:
#       print(iterator)
#       print(next(iterator)) # prints the value
#     except StopIteration:
#       break

# special_for([1,2,3])

# OUR OWN RANGE
class MyGen():
  current = 0   # Where we are on iteration
  def __init__(self, first, last):
    self.first = first
    self.last = last

  def __iter__(self):
    return self
  
  def __next__(self):
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration

gen = MyGen(0, 100)
for i in gen:
  print(i)

