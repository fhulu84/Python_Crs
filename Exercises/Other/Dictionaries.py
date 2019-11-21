# DICTIONARY
user = {
    'basket': [1, 2, 3],
    'greeting': 'hello',
    'age': 20
}

# print(user['weapons'][1])

# my_list = [
#     {
#         'a': [1, 2, 3],
#         'b': 'hello',
#         'x': True
#     },
#     {
#         'a': [4, 5, 6],
#         'b': 'bye',
#         'x': False
#     }
# ]
# print(my_list[0]['a'][2])

# dictionary2 = dict(name='JohnJohn')
# print(dictionary2)

# IN
# print('basket' in user)

# IN keys
# print('basket' in user.keys())

# IN values
# print('hello' in user.values())

# ITEMS
# print(user.items())

# CLEAR
# user.clear()
# print(user) #prints none

# COPY
# user2 = user.copy()

# print(user.clear())
# print(user2)

# POP
# print(user.pop('age'))
# print(user.popitem())

# UPDATE
user.update({'age': 55})
user.update({'ages': 55})

print(user)
