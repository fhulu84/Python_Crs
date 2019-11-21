from datetime import datetime

birth_year = input('What year were you born? ')

age = datetime.now().year - int(birth_year)

print(f'You are {age} years old.')
