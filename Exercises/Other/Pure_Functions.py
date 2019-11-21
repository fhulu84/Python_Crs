# some useful functions that allow us to think in a functional programming paradigm
# map, filter, zip and reduce

# Pure Function
# def multiply_by2(li):
#   new_list = []
#   for item in li:
#     new_list.append(item*2)
#   return new_list

# print(multiply_by2([1,2,3]))

# map
my_list = [1, 2, 3]


def multiply_by2(item):
    return item*2


print(list(map(multiply_by2, my_list)))  # [2,4,6]
# [1,2,3], pure function doesnt affect the outside world
print(my_list)
