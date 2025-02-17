num = 700000
while num != 701000:
    m = []
    for delitel in range(2,num //2+1):
        if num % delitel == 0: m.append(delitel)
    if len(m) == 0: m = 0
    else :
        m = min(m) + max(m)
    if m % 10 == 8: print(num, m)
    num += 1


