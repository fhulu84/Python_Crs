# list, set, dictionary comprehensions

#Format: my_list = [param for param in iterable]

# LIST
# my_list = [char for char in 'hello']
# my_list2 = [num for num in range(0,50)]
# my_list3 = [num**2 for num in range(0,50)]
# my_list4 = [num**2 for num in range(0,50) if num % 2 == 0]

# print(my_list)
# print(my_list2)
# print(my_list3)
# print(my_list4)

# SET

# my_list = {char for char in 'hello'}
# my_list2 = {num for num in range(0,50)}
# my_list3 = {num**2 for num in range(0,50)}
# my_list4 = {num**2 for num in range(0,50) if num % 2 == 0}

# print(my_list)
# print(my_list2)
# print(my_list3)
# print(my_list4)

# DICTIONARY
simple_dict = {
  'a': 1,
  'b': 2
}
my_dict = {k:v**2 for k,v in simple_dict.items()}
my_dict2 = {k:v**2 for k,v in simple_dict.items() if v%2==0}
my_dict3 = {num:num*2 for num in [1,2,3]}

print(my_dict)
print(my_dict2)
print(my_dict3)

