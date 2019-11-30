# Given two strings, s1 and s2, create a mixed String
# create a third-string picking the first char in line from first,
# second char in line from second
# Any leftover chars go at the end of the result.

def mix_strings(s1, s2):
  result = ''
  s2 = s2[::-1]    # reverse second string
  print(s2)
  max_len = len(s1) if len(s1) > len(s2) else len(s2) # calc max_len

  for i in range(max_len):
    if i < len(s1):
      result += s1[i]
    if i < len(s2):
      result += s2[i]

  return result

str1 = 'Pynative'
str2 = 'Website'

print(mix_strings(str1, str2))
