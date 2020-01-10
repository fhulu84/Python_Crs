import re

string = 'search this inside of this text please!'

# print('search' in string) # True, simple way to search 

# re.search returns None when nothing found
# a = re.search('this', string)
# print(a.span()) # (7, 11) index numbers, the one found first
# print(a.start()) # 7
# print(a.end())   # 11
# print(a.group()) # this (matched text)

# pattern = re.compile('search this')
# a = pattern.search(string)
# b = pattern.findall(string) # ['this', 'this'] (finds all the instinces of the match)
# c = pattern.fullmatch(string) # None (if you compile the pattern with whole content of string, then it would return an object) 
# d = pattern.match(string) # None (searches for the match in the beginning, if found then returns an object (try with 'search this'))
# print(d)

# pattern = re.compile(r"(\d).([a-z])") #r means raw string, to ignore special characters like /.'
# test_str = "Test 1kalem 2 silgi 3 Defter"

# a = pattern.search(test_str)
# print(a.group()) # 1ka

# Email validator
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'b@b.com'

a = pattern.search(string)
print(a)
