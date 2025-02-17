from itertools import product
count = 0
for word in product('СВЕТА', repeat = 5):
    predicate = word.count('С') >= 1
    if predicate:
        count += 1
print(count)