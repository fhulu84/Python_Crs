# Given a list iterate it and count the occurrence of each element and 
# create a dictionary to show the count of each element

my_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
my_dict = {}

for item in my_list:
  my_dict[item] = my_list.count(item)

print(f'Original list: {my_list}')
print(f'Count of each item: {my_dict}')