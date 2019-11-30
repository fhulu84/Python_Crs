# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order

def rev_word_order(s):
  return ' '.join(s.split()[::-1])


string = input('Enter a string containing multiple words: ')

print()
print(f'Words in reverse order: {rev_word_order(string)}')
