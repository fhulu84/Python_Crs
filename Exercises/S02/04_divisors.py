# Create a program that asks the user for a number and then prints out a list of all the divisors of that number

num = int(input('Enter a number: '))

print(f'Divisors of {num}: ', end='')
print([d for d in range(1, num+1) if num % d == 0])