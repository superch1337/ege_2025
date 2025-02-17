a = []
for n in range(1000):
    b = bin(n)[2::]
    if n % 2 == 0:b += "00"
    else:b += "11"
    result = int(b,2)
    if result > 134:
        a.append(n)
print(min(a))