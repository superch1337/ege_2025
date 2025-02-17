ans = []
for n in range(1000, 10000):
    b = str(n)
    res_1 = int(b[0]) + int(b[1])
    res_2 = int(b[1]) + int(b[2])
    res_3 = int(b[2]) + int(b[3])
    a = sorted([res_1,res_2,res_3])
    a.pop(0)
    res = str(a[0]) + str(a[1])
    if res == "1315":
        ans.append(n)
print(max(ans))