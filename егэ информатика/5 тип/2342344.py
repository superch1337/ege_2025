ans = []
for n in range(1000):
    b = bin(n)[2::]
    b += str(b.count("1")%2)
    b += str(b.count("1") % 2)
    r = int(b,2)
    if r > 83:
        ans.append(r)
print(min(ans))