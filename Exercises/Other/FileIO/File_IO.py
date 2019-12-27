# I/O => in/out

# my_file = open('test.txt')
# # print(my_file.read())
# # my_file.seek(0) # set cursor at the beginning of the file
# # print(my_file.read())
# # my_file.seek(0) # set cursor at the beginning of the file
# # print(my_file.read())

# # print(my_file.readline())
# # print(my_file.readline())
# # print(my_file.readline())

# print(my_file.readlines()) # list contains whole content of the file
# my_file.close() # we have to close it after we've done 

# you dont need to close the file explicitly with with
# with open('test.txt') as my_file:
#   print(my_file.readlines())

# READ(r) & WRITE(r+/w)
# with open('test.txt', mode='r+') as my_file:
#   text = my_file.write('hey it\'s me!') # starts from the beginning of the file, if it's not empty it overrides the characters
#   print(text) # prints 12, number of characters written

# APPEND(a)
# with open('test.txt', mode='a') as my_file:
#   text = my_file.write('Hello it\'s me!')

# with open('sad.txt', mode='w') as my_file: # w: creates a new file/overrides and write to it, r+:FileNotFoundError
#   text = my_file.write(':(')

# app/sad.txt --> relative path
# /Users/User/Desktop/HILAL/STUDY/WEB/UDEMY/Python_Crs/Exercises/Other/FileIO/app/sad.txt --> absolute path
# ./app/sad.txt --> from current folder to app to sad.txt
# ../app/sad.txt --> back a folder to app to sad.txt
try:
  with open('sad.txt', mode='r') as my_file: 
    print(my_file.read())
except FileNotFoundError as err:
  print('file does not exist')
  raise err # run the error
except IOError as err: #usually happens when your computer has some issues of any sort of IO operation
  print('IO error')

##########
# pathlib builtin module - object oriented filesystem paths, same code works for different operating systems
##########


