def f(x,y,d):
    if x == y: return 1
    if x > y or x == 30: return 0
    else: return f(x+d,y,d) + f(x*2,y,d)
mass = []
for d in range(1,100):
    mass.append(f(1,10,d)*f(10,100,d))
print(sum(mass))
