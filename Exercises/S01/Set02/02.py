# Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1

def append_middle(str1, str2):
  middle = int(len(str1) / 2) if len(str1)%2 == 0 else int(len(str1) / 2) + 1 # middle index
  return str1[:middle] + str2 + str1[middle:]


str1 = 'Chrisdem'
str2 = 'IamNewString'

print(append_middle(str1, str2))

str1 = 'Hello'
str2 = 'Omer'

print(append_middle(str1, str2))

