from itertools import product

ans = 0
chet = '02468A'
nechet = '13579B'
for word in product('0123456789AB', repeat = 6):
    word = ''.join(word)
    predicate = word.count("B") == 1 and word[0] != '0'
    predicate2 = len([i for i in word if i in chet]) == len([i for i in word if i in nechet])
    if predicate and predicate2: ans += 1
print(ans)
