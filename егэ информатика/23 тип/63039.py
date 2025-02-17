def f(x,y,z):
    if x == y: return 1
    if x > y+1: return 0
    else:
        if len(z) > 0 and z[-1] == "a": return f(x*2,y,z+'b') + f(x*3,y,z+'c')
        else: return f(x-1,y,z+'a') + f(x*2,y,z+'b') + f(x*3,y,z+'c')

print(f(3,20,''))