from itertools import product

count = 0
for word in product('ИВАН',repeat = 5):
    predicate = word.count('И') > 0
    if predicate:
        count += 1
print(count)