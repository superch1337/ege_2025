import sys
sys.setrecursionlimit(10**8)

def f(n):
    if n < 11: return 10
    return n+f(n-1)
print(f(2124)-f(2122))