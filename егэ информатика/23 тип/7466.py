def f(x,y):
    if x == y: return 1
    if x > y or x == 29: return 0
    else: return f(x+1,y) + f(x+2,y)+ f(x+4,y)
print(f(21,30))