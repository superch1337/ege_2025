from itertools import product

count = 0

for word in product("ABCX", repeat = 5):
    if 0 < word.count("X") < 2:
        if word[-1] == "X":
            count += 1
    if "X" not in word:
        count +=1

print(count)