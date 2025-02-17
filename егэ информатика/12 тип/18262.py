from random import shuffle

def f(a):
    if ',' in str(a**0.5): return False
    return True

ans = []

for n in range(200):
    stroka = list(n * '3' + 17 * '0' + 17 * '2')
    shuffle(stroka)
    stroka = '>' + ''.join(stroka)
    while '>3' in stroka or '>2' in stroka or '>0' in stroka:
        if '>3' in stroka: stroka = stroka.replace('>3','22>',1)
        if '>2' in stroka: stroka = stroka.replace('>2', '2>', 1)
        if '>0' in stroka: stroka = stroka.replace('>0', '3>', 1)
    suma = sum([int(i) for i in stroka if i != '>'])
    if f(suma):
        ans.append(n)
print(min(ans))