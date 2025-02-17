ans = []
for n in range(1000000):
    b = bin(n)[2::]
    if n % 5 == 0:
        b = b + bin(5)[2::]
    else:
        b += '1'
    if int(b , 2) % 7 == 0:
        b += bin(7)[2::]
    else:
        b += '1'
    R = int(b, 2)
    if R < 1855663:
        ans.append(n)
print(max(ans))
