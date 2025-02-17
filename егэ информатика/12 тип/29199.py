from random import *
for i in range(100):
    stroka = [12 * "1" + 15 * "2" + 17 * "3"]
    shuffle(stroka)
    stroka = '0'+''.join(stroka)
    while '01' in stroka or '02' in stroka or '03' in stroka:
        stroka = stroka.replace('01','20',1)
        stroka = stroka.replace('02', '120', 1)
        stroka = stroka.replace('03', '302', 1)
    print(f'ans- {stroka.count('1')}')