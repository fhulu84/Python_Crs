# some useful functions that allow us to think in a functional programming paradigm
# map, filter, zip and reduce

# Pure Function
# def multiply_by2(li):
#   new_list = []
#   for item in li:
#     new_list.append(item*2)
#   return new_list
# print(multiply_by2([1,2,3]))

from functools import reduce  # we need to import it to be able to use reduce

my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = (5, 4, 3)

# MAP
# def multiply_by2(item):
#     return item*2

# print(list(map(multiply_by2, my_list)))  # [2,4,6]
# # [1,2,3], pure function doesnt affect the outside world
# print(my_list)

# FILTER
# def only_odd(item):
#     return item % 2 != 0

# print(list(filter(only_odd, my_list)))

# ZIP
# print(list(zip(my_list, your_list, their_list)))

# REDUCE


def accumulator(acc, item):
    return acc + item


print(list(reduce(accumulator, my_list, 0)))  # 0 1
# 1 2
# 3 3
# 6
