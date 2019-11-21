def highest_even(numbers):
  '''
    Info: returns highest even number in the given list
  '''
  evens = []
  for number in numbers:
    if number % 2 == 0:
      evens.append(number)
  return max(evens)

print(highest_even([10,2,3,4,5,11]))