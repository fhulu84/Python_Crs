# Return the number of times that the string “Emma” appears anywhere in the given string

def count_word(sentence, word):
  sentence = sentence.upper() # case insensitive search
  word = word.upper()
  return sentence.count(word)

sentence = 'Emma is a good developer. Emma is also a writer'
word = 'emma'
print(f'{word} appeared {count_word(sentence, word)} times')