# Remove duplicate from a list and create a tuple and find the minimum and maximum number

my_list = [87, 52, 44, 53, 54, 87, 52, 53]

print(f'Original list: {my_list}')

uniques = list(set(my_list))
print(f'Unique items: {uniques}')
print(f'Tuple: {tuple(uniques)}')
print(f'min: {min(uniques)}')
print(f'max: {max(uniques)}')


