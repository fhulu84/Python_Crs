# Given a following two sets find the intersection and remove those elements from the first set

set1 = {65, 42, 78, 83, 23, 57, 29}
set2 = {67, 73, 43, 48, 83, 57, 29}

intersect = set1.intersection(set2)
print(f'First set: {set1}')
print(f'Second set: {set2}')
print()
print(f'Instersection: {intersect}')

for i in intersect:
  set1.remove(i)
print(f'First set after removing intersection elements: {set1}')

