# Iterate a given list and Check if a given element already exists 
# in a dictionary as a key’s value if not delete it from the list

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
my_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

print(f'List: {roll_number}')
print(f'Dictionary: {my_dict}')

roll_number[:] = [item for item in roll_number if item in my_dict.values()]
# roll_number = [item for item in roll_number if item in my_dict.values()] - same result
print(f'Unwanted removed: {roll_number}')