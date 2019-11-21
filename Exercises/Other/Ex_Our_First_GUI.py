picture = [
	[0, 0, 0, 1, 0, 0, 0],
	[0, 0, 1, 1, 1, 0, 0],
	[0, 1, 1, 1, 1, 1, 0],
	[1, 1, 1, 1, 1, 1, 1],
	[0, 0, 0, 1, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0],
]

# print('Hello', end='') #end='\n' in default so it jumps to new line
# print(' Hilal')

# for row in picture:
# 	for pixel in row:
# 		if (pixel == 0):
# 				print(' ', end = '')
# 		elif (pixel == 1):
# 				print('*', end = '')
# 	print('')

# Cleaner version
fill = '*'
empty = ' '
for row in picture:
	for pixel in row:
		if pixel:
				print(empty, end = '')
		else:
				print(fill, end = '')
	print('')