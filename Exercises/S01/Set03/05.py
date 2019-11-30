# Given a two list of equal size create a set such that it shows the element from both lists in the pair

list_1 = [2, 3, 4, 5, 6, 7, 8]
list_2 = [4, 9, 16, 25, 36, 49, 64]

print(f'First List: {list_1}')
print(f'Second List: {list_2}')
print(f'Result: {set(zip(list_1, list_2))}')

# zip: paralel iteration