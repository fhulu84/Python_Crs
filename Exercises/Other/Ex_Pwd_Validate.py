import re

pattern = re.compile(r'[A-Za-z0-9$%#@]{7,}\d')
# pattern = re.compile(r'[A-Za-z0-9$%#@]{7,}[0-9]') #alternative way
string = 'Hilal'
string2 = 'dfrt456%#23'

a = pattern.search(string)
a2 = pattern.fullmatch(string2)
print(a)
print(a2)

# At least eight characters long
# contain any sort letters, numbers $%#@
# has to end with a number