def f(x,y):
    if x == y: return 1
    if x < y or x == 24: return 0
    else: return f(x -2,y) + f(x-3,y) + f(x//4,y)
print(f(36, 13))