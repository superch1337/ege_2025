def f(n):
    if n == 1: return 5
    if n == 2: return 5
    if n > 2: return 5*f(n-1)-4*f(n-2)
print(f(13))