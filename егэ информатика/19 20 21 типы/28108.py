def f(x,h):
    if x > 30: return h%2 == 0
    if h == 0: return 0
    listH = [f(x+1,h-1),f(3*x-2,h-1)]
    return any(listH) if (h-1)%2==0 else all(listH)
# print(f'19. {min(s for s in range(2,30) if not f(s,1) and f(s,2))}')
print(f'20. {[s for s in range(2,30) if not f(s,1) and f(s,3)]}')
print(f'20. {min([s for s in range(2,30) if not f(s,2) and f(s,4)])}')