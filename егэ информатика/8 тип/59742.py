from itertools import product
count = 0
nechet = ['1','3','5','7','9']
chet = ['2','4','6','8']
for word in product('0123456789', repeat = 4):
    predicate1 = len(set([i for i in word])) == 4
    flag = True
    for i in range(0,len(word)):
        if