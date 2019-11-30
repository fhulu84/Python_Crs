# Given two sets, Checks if One Set is Subset or superset of Another Set. 
# if the subset is found delete all elements from that set

set1 = {57, 83, 29}
set2 = {67, 73, 43, 48, 83, 57, 29}

print(f'First set: {set1}')
print(f'Second set: {set2}')
print()

print(f'First set is subset of second set: {set1.issubset(set2)}')
print(f'Second set is subset of first set: {set2.issubset(set1)}')
print()

print(f'First set is super set of second set: {set1.issuperset(set2)}')
print(f'Second set is super set of first set: {set2.issuperset(set1)}')
print()

if set1.issubset(set2):
  set1.clear()

if set2.issubset(set1):
  set2.clear()

print(f'First set: {set1}')
print(f'Second set: {set2}')
