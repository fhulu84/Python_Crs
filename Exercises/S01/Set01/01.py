# Accept two int values from the user and return their product. 
# If the product is greater than 1000, then return their sum

def multiplication_or_sum(num1, num2):
  product = num1 * num2
  if product > 1000:
    return num1 + num2
  return product

num1 = int(input('Enter first number '))
num2 = int(input('Enter second number '))

print(f'The result is {multiplication_or_sum(num1, num2)}')
