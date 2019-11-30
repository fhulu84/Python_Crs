# Write one line of Python that takes a list a and makes a new list 
# that has only the even elements of this list in it.

import random

a = [n for n in random.sample(range(1,100), k=20)]

print(a)
print([n for n in a if n % 2 == 0])