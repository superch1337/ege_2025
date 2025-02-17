def c(a):
    for i in range(1000):
        if i*i > a: return i-1
        if i*i == a: return i
def f(x,y):
    if x ==y: return 1
    if x < y: return 0
    else: return f(x-4,y) + f(x-7,y) + f(c(x),y)
print(f(44,22)*f(22,3))