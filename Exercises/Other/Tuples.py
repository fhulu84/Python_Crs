# TUPLE
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[2])
# print(5 in my_tuple) 

# TUPLE key in DICT
# user = {
#     (1,2): [1,2,3],
#     'greet': 'hello'
# }

# user[(1,2)][2] = 5
# print(user[(1,2)])

# TUPLE like LIST
my_tuple = (1,2,3,4,5,5)

# new_tuple = my_tuple[1:2] # output(2,) a tuple with only one item
# print(new_tuple)

# x,y,*other,z = (1,2,3,4,5)
# print(x)
# print(y)
# print(other)
# print(z)

print(my_tuple.count(5)) # 2
print(my_tuple.index(5)) # 4
print(len(my_tuple)) # 6



