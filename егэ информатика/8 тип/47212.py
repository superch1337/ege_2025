from itertools import product

count = 0
for word in product("01234567", repeat = 5):
    if word[0] != "0" and word.count("6") == 1:
        chet = '246'
        for i in range(len(word) - 1):
            if i == 0:
                if word[i] == '6' and word[i+1] in chet:
                    count += 1
            elif i == 4:
                if word[i-1] in chet and word[i] == '6':
                    count += 1
            else:
                if word[i - 1] in chet and word[i] == '6' and word[i+1] in chet:
                    count += 1
print(count)