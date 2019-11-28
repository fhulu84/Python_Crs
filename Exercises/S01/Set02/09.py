# Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters

def print_sum_and_avg(str):
  sum = 0
  count = 0
  words = str.split()

  for word in words:
    if(word.isdigit()):
      sum += int(word)
      count += 1
  
  print(f'Sum = {sum}, average = {sum/count}')


input_str = 'English = 78 Science = 83 Math = 68 History = 65'
print_sum_and_avg(input_str)

# Solution2, to get all numbers
print([int(s) for s in input_str.split() if s.isdigit()])

# Solution 3 (regex)
import re
print([int(num) for num in re.findall(r'\b\d+\b', input_str)])







