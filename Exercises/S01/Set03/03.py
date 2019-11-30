# Given a list slice it into a 3 equal chunks and rever each list

my_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk_size = int(len(my_list) / 3)

print(f'Original list: {my_list}')
chunk_1 = my_list[:chunk_size]
print(f'Chunk 1 : {chunk_1}')
print(f'After reversing it: {chunk_1[::-1]}')
chunk_2 = my_list[chunk_size: 2*chunk_size]
print(f'Chunk 2: {chunk_2}')
print(f'After reversing it: {chunk_2[::-1]}')
chunk_3 = my_list[2*chunk_size:]
print(f'Chunk 3: {chunk_3}')
print(f'After reversing it: {chunk_3[::-1]}')