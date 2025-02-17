ans = []

for n in range(100,1000):
    newstr = str(n)
    n1 = int(newstr[0]) + int(newstr[1])
    n2 = int(newstr[1]) + int(newstr[2])
    if n1 < n2: newstr = str(n1) + str(n2)
    else: newstr = str(n2) + str(n1)
    if newstr == "1115": ans.append(n)
print(min(ans))