from itertools import product
nechet = "1357"
count = 0
for word in product("012345678",repeat = 5):
    word = ''.join(word)
    if word.count("3") == 2 and word[0] != "0":
        flag = 1
        for i in word:
            if i in nechet:
                word = word.replace(i,"*")
        if "2*" in word or "*2" in word:
            flag = 0
        if flag == 1: count += 1

print(count)