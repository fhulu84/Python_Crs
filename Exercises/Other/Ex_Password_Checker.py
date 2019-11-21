import getpass

username = input('Username: ')
password = getpass.getpass('Password: ')

password_length = len(password)
hidden_password = '*' * password_length

print(f'{username}, your password, {hidden_password}, is {password_length} letters long')
