# Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list

my_list = [34, 54, 67, 89, 11, 43, 94]

print(f'Original list: {my_list}')
item = my_list.pop(4)
print(f'Element at index 4 removed: {my_list}')
my_list.insert(2, item)
print(f'Element added at index 2: {my_list}')
my_list.append(item)
print(f'Element added at last: {my_list}')