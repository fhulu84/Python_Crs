# DECORATOR Pattern

# def hello():
#     print('Helloooo')


# greet = hello     # greet points to location of hello in memory
# del hello         # deleted the hello pointer

# print(greet())    # print out hello function, since it still points it
# print(hello())    # hello pointer deleted so this throws an error

# def hello(func):
#   func()

# def greet():
#   print('still here!')

# a = hello(greet)

# print(a)             # runs greet function

# HIGHER ORDER FUNCTIONS (HOC)
# def greet(func):
#   func()

# def greet2():
#   def func():
#     pass
#   return func

# MAP, REDUCE, FILTER are HOC

# DECORATORS has their power from functions' ability being like a variable, like a firstclass citizens

# def my_decorator(func):
#     def wrap_func():     # it gives us more flexibility and to be able to add more functionality
#         print('*********')
#         func()
#         print('*********')
#     return wrap_func


# @my_decorator        # like hello2 = my_decorator(hello) then hello2()
# def hello():
#     print('Helloooo')


# @my_decorator
# def bye():
#     print('see ya later')

# hello()
# bye()

# WITH ONE PARAMETER
# def my_decorator(func):
#     def wrap_func(x):     # it gives us more flexibility and to be able to add more functionality
#         print('*********')
#         func(x)
#         print('*********')
#     return wrap_func


# @my_decorator        
# def hello(greeting):
#     print(greeting)

# hello('hellloooo')

# WITH MULTI-PARAMETERS and KEYWORDs

def my_decorator(func):
    def wrap_func(*args, **kwargs):     # it gives us more flexibility and to be able to add more functionality
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_func


@my_decorator        
def hello(greeting, emoji=':('):
    print(f'{greeting} {emoji}')

hello('hellloooo')