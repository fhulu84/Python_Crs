# linting     -> like pylint shows errors when writing the code

# ide/editor  -> using an ide or editor like pycharm, vscode ...

# read errors -> to be able to understand the errors, there are 15-20 most common error types, check documentation

# pdb         -> using pyhton debugger

import pdb

def add(num1, num2):
  pdb.set_trace()
  t = 4*5
  return num1 + num2

print(add(4, 'jgsjdfjgs'))


