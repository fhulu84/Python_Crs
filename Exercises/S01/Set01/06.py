# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

def print_div_by_5(li):
  for num in li:
    if num % 5 == 0:
      print(num)

my_list = [1, 3, 5, 10, 37, 53, 30, 15, 8]
print(my_list)
print('Finding divisible of 5')
print_div_by_5(my_list)