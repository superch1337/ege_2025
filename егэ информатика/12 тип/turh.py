ans = []
for n in range(3,10000):
    stroka = '1' + '2'*n
    while "12" in stroka or "322" in stroka or "222" in stroka:
        if "12" in stroka: stroka = stroka.replace("12","2",1)
        if "322" in stroka: stroka = stroka.replace("322","21",1)
        if "222" in stroka: stroka = stroka.replace("222","3",1)
    if sum([int(i) for i in stroka]) == 15: ans.append(n)
print(min(ans))