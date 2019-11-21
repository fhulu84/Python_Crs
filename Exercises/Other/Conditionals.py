age = int(input('What is your age? '))
is_licensed = True

if(age >= 21 and is_licensed): # and,or usage
    print('You can be a qualified driver')
elif(age < 17):
    print(f'You have to wait {17-age} years to be a learner driver')
else:
    print(f"You have to wait {21-age} years to be a qualified driver")

# Ternary Operator
is_eligible = True if (age > 21) else False
print(is_eligible)
