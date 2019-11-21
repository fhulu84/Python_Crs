# BREAK, CONTINUE, PASS
i = 10
while i > 0:
    if i == 2:
        break
    if i == 5:
        i -= 1
        continue
    if i == 4:
        pass #thinking about sth here but not decided yet
    print(i)
    i -= 1
else:
    print(f'all done until i = {i}') #this part only runs when the while block executed until the end without a break

#INDEFINITE LOOP
# while True:
#     response = input('Continue?(yes or no): ')
#     if(response == 'yes'):
#         break