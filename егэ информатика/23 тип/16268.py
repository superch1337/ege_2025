def f(x,y):
    if x == y: return 1
    if x > y or x == 13: return 0
    else: return f(x+2,y)+ f(x*3,y) + f(x*x,y)
print(f(3,49))
