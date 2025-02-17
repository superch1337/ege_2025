def f(x,y):
    if x == y: return 1
    if x > y or x == 6: return 0
    else: return f(x +1, y) + f(x +2, y) + f(x *2, y)
print(f(4,15)*f(15,19))
