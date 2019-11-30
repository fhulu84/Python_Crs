# Given a list of ints, return True if first and last number of a list is same

def is_first_last_same(li):
  return li[0] == li[-1]

my_list = [1,2,3,4,5,1]
print(f'is the first and last number of {my_list} same?')
print(f'Result is {is_first_last_same(my_list)}')