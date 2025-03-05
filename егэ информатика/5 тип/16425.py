for i in range(1,3000):
    b = bin(i)[2:]
    b = b[:-1]
    if i % 2 == 0: b += '01'
    else: b += '10'
    res = str(int(b,2))
    if res == '2017': print(i)



