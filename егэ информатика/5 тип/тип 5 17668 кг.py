ans = []
for N in range(1000):
    b = bin(N)[2:]
    if b.count("1") % 2 == 0: b = '10' + b[2:] + '0'
    else: b = '11' + b[2:] + '1'
    if N > 27: ans.append(int(b, 2))
print(min(ans))