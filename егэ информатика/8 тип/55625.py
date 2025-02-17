from itertools import product

count = 0
strgl = "ЯОА"
strsogl = "РСЛВ"

for word in product("ЯРОСЛАВ",repeat = 5):
    gl = set([i for i in word if i in strgl])
    sogl = set([i for i in word if i in strsogl])
    flag = 1
    for i in range(len(word)-1):
        if word[i] in strgl and word[i+1] in strgl:flag = 0
    if len(gl) < len(sogl) and len(gl) + len(sogl) == 5 and flag == 1:count += 1

print(count)
