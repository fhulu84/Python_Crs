# RANGE
# print(range(100)) #(0,100)

# for _ in range(0,10,2):
#     print(_)           # 0,2,4,6,8

# for _ in range(10,0,-2):
#     print(_)

# for _ in range(10,0,-2):
#     print(list(range(10))) # 5 times [0,1,...,9]

#ENUMERATE
# for i,char in enumerate('Hellooo'):
#     print(f'{i}: {char}')

for i,item in enumerate(list(range(100))):
    if(i == 50):
        print(f'{i}: {item}')