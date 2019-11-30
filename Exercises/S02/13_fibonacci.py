def fibonacci(count):
  pre1 = 0
  pre2 = 1

  for i in range(count):
    yield pre2
    temp = pre1
    pre1 = pre2
    pre2 = temp + pre2

count = int(input('How many fibonacci numbers do you want to generate: '))

fib_nums = []
for num in fibonacci(count):
  fib_nums.append(num)

print(fib_nums)

# RECURSIVE FUNCTION CALL
def fib(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fib(n-1) + fib(n-2)

fib_nums = []
for i in range(1, num+1):
  fib_nums.append(fib(i))

print(fib_nums)

    
