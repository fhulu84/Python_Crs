# Find all occurrences of “USA” in given string ignoring the case

def count_word(sentence, word):
  sentence = sentence.upper() # case insensitive search
  word = word.upper()
  return sentence.count(word)

sentence = 'Welcome to USA. usa awesome, isn\'t it?'
word = 'USA'
print(f'{word} appeared {count_word(sentence, word)} times')