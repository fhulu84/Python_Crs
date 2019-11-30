# Accept string from the user and display only those characters which are present at an even index

def print_chars_even_index(str):
  for i in range(0, len(str), 2):
    print(f'index[ {i} ] {str[i]}')

my_str = input('Enter String ')
print(f'Original String {my_str}')

print('Printing only even index chars')
print_chars_even_index(my_str)
