# Ask the user for a number and determine whether the number is prime or not.

def is_prime(n):
  if n > 1:
    divisors = [d for d in range(1, n+1) if n % d == 0]
    if len(divisors) == 2: # 1 and number itself
      return True
  
  return False

number = int(input('Enter a number: '))

msg = 'a PRIME' if is_prime(number) else 'NOT a PRIME'

print(f'{number} is {msg} number')
