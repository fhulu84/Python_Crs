# amazon_cart = [
#     'notebooks',
#     'sunglasses',
#     'toys',
#     'grapes'
# ]

# amazon_cart[0] = 'laptop'
# new_cart = amazon_cart[0:3]
# new_cart = amazon_cart #it is like a pointer they show the same place in memory, this doesnt copy the values into the other list

# this way you can copy the entire list values into the other list
# new_cart = amazon_cart[:]

# new_cart[0] = 'gum'

# print(new_cart)
# print(amazon_cart)

basket = [1, 2, 3, 4, 5]
basket2 = ['a', 'b', 'c', 'd', 'e']

# LEN
# print(len(basket))

# APPEND
# basket.append(100)
# new_list = basket
# print(basket)
# print(new_list)

# INSERT
# basket.insert(1, 100)
# new_list = basket
# print(basket)
# print(new_list)

# EXTEND
# basket.extend([100, 101])
# new_list = basket
# print(basket)
# print(new_list)

# -----REMOVING------
# POP
# basket.extend([100])
# basket.pop()
# print(basket)
# basket.pop(2)
# print(basket)

# CLEAR
# basket.clear()
# print(basket)

# INDEX
# print(basket2.index('d'))
# print(basket2.index('d', 2, 10))

# IN
# print('d' in basket2)  # True
# print('x' in basket2)  # False
# print('i' in 'Hello my name is Hilal')

# COUNT
# basket2.append('d')
# print(basket2.count('d'))

# SORT. SORTED, COPY
basket2.extend(['d', 'c', 'f'])
basket2.insert(2, 'x')
# basket2.sort()
# print(basket2)
# print(sorted(basket2))
# print(basket2)
# new_basket = basket2[:]
# new_basket = basket2.copy()
# new_basket.sort()
# print(new_basket)
# print(basket2)

# REVERSE
# basket2.reverse() # just reverse the list, not sorts it
# print(basket2)

# RANGE
# print(list(range(1, 20)))
# print(list(range(21)))

# JOIN
# sentence = ' '
# new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Hilal'])
# new_sentence2 = ' '.join(['hi', 'my', 'name', 'is', 'Hilal']) # in short

# print(new_sentence)
# print(new_sentence2)

# LIST UNPACKING
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(other)
print(d)
