# for item in 'Zero to Mastery':
#     print(item)

# sum = 0
# for item in [1,2,3,4,5]:
#     sum += item
# print(sum)

# list1 = [1,2,3]
# list2 = [1,2,3]

# sum = 0
# for i in list1:
#     for j in list2:
#         sum += i*j
# print(sum)

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user:
    print(user[item])

for k, v in user.items():
    print(k, v )

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)
