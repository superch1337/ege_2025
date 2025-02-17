from itertools import product
count = 0
for word in product("ABCDXYZ", repeat = 4):
    if word[0] in 'XYZ' and word[1] in 'XYZ' and word[2] in 'ABCD' and word[3] in 'ABCD':
        count += 1
print(count)
