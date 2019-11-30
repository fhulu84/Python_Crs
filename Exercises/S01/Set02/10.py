# Given an input string, count occurrences of all characters within a string

def count_chars(str):
  result = {}
  
  for c in str:
    result[c] = str.count(c)

  print(result)

count_chars('pynativepynvepynative')
