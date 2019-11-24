# RANGE
def fib(number):
  a = 0
  b = 1
  for i in range(number + 1):
    yield a
    temp = a
    a = b
    b = temp + b

for item in fib(20):
  print(item)

# LIST
def fib2(number):
  a = 0
  b = 1
  result = []
  for i in range(number + 1):
    result.append(a)
    temp = a
    a = b
    b = temp + b
  return result

for item in fib2(20):
  print(item)