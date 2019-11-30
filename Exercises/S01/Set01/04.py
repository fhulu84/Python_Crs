# Given a string and an int n, remove characters from string starting from zero up to n and return a new string

def remove_chars(str, n):
  return str[n:]


print(f'Removing n of chars')
print(remove_chars('pynative', 4))
