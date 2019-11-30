# String characters balance Test
# We’ll say that a String s1 and s2 is balanced if all the chars in the string1 are there in s2. 
# characters position doesn’t matter

def is_string_balanced(s1, s2):
  for c in s1:
    if s2.count(c) == 0:
      return False
  return True

str1 = 'yn'
str2 = 'Pynative'
print(is_string_balanced(str1, str2))

str1 = 'yng'
str2 = 'Pynative'
print(is_string_balanced(str1, str2))