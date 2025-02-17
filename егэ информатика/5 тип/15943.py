lst = []
def summa(a):
    b = len(a)
    result = 0
    while b != 0:
        result += int(a[b-1])
        b -= 1
    a += str(result%2)
    return a
for n in range(1000):
    b = bin(n)[2::]
    b = b + b[-1]
    b = summa(b)
    r = int(b, 2)
    if r > 105: lst.append(r)
print(min(lst))