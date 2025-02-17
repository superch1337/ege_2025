def s(a):
    mas = []
    for i in range(1,1000):
        if a % i == 0:
            mas.append(i)
    return sum(mas)

def f(x,y):
    if x == y: return 1
    if x > y: return 0
    else: return f(x+1,y) + f(s(x),y)
print(f(2,24))