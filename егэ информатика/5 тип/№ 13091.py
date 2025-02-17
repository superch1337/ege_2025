ans = []
for n in range(65):
    b = bin(n)[2::]
    b += bin(n % 4)[2::]
    r = int(b, 2)
    ans.append(r)
print()