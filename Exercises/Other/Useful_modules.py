from collections import Counter, defaultdict, OrderedDict
import datetime
from time import time # We used this in Decorators_2.py
from array import array

# COUNTER
# it is really useful when finding duplicate emails or usernames

li = [1,2,3,4,5,6,7,7]
print(Counter(li))

sentence = 'blah blah blah thinking about python'
print(Counter(sentence))

# defaultdict
# in dict d['c'] throws error since this keyword doesnt exist, to prevent this use defaultdict
# defaultdict(callable object,dict); callable object can be e.g. int, in this case absent keyword returns 0
# callable object can be a lambda function, we dont need
dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b':2})
print(dictionary['c']) # returns -1

# OrderedDict
# Keeps dictionary ordered(entry order)
# Regular dictionary(dict) in python doesnt have sense of order
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1


print(d2 == d) # False, because order is different, result would be True for regular dictionaries

# datetime
print(datetime.time()) #00:00:00
print(datetime.time(2,3,25)) #02:03:25
print(datetime.date.today()) #2019-12-22 

# array
# performs faster than list, but list is more flexible
# if you dont wanna use generators, if you have a massive list, this is a quick way to optimize ypur code

arr = array('i', [1,2,3])
print(arr[0])
