from itertools import product
count = 0
for word in product('ABX', repeat = 6):
    predicate = word.count('X') == 1
    if predicate: count += 1
print(count)