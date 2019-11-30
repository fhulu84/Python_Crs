# Given a two list of ints create a third list 
# such that should contain only odd numbers from the first list and even numbers from the second list

def merge_lists(li1, li2):
  odds_li1 = list(filter(lambda n: n%2 != 0, li1))
  evens_li2 = list(filter(lambda n: n%2 == 0, li2))
  return odds_li1 + evens_li2

list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]

print('Merged list is')
print(merge_lists(list1, list2))