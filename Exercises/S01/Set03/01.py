# Given a two list. 
# Create a third list by picking an odd-index element from the first list and even index elements from second.


list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

print(f'Element at odd-index positions from list1\n{list1[1::2]}')
print(f'Element at odd-index positions from list2\n{list2[0::2]}')

print(f'Printing Final third list\n{list1[1::2] + list2[::2]}')
