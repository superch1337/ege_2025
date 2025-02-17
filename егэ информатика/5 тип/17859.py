ans = []
for n in range(1000): 
    b = bin(n)[2::]
    if b.count("1") % 2 == 0:
        b = "10" + b
    else: 
        b = "1" + b + "01"
    R = int(b, 2)
    if n < 12: ans.append(R)
print(max(ans))