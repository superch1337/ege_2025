ans = []
for n in range(1000):
    c, b = 2, bin(n)[2:]
    while c != 0: a = b.count("1"); b += str(a%2); c -= 1
    if int(b, 2)> 85: ans.append(n)
print(min(ans))