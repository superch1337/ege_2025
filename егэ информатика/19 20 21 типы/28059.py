def f(x,h):
    if x >= 27: return h%2 == 0
    if h == 0: return 0
    listH = [f(x+1,h-1),f(x+2,h-1),f(x*2,h-1)]
    return any(listH) if (h-1)%2 == 0 else any(listH)
def f1(x,h):
    if x >= 27: return h%2 == 0
    if h == 0: return 0
    listH = [f1(x+1,h-1),f1(x+2,h-1),f1(x*2,h-1)]
    return any(listH) if (h-1)%2 == 0 else all(listH)
print(f'19. {min(s for s in range(1,26+1)if not f(s,1) and f(s,2))}')
print('20.',*[s for s in range(1,26+1) if not f1(s,1) and f1(s,3)])
print(f'20. {min([s for s in range(1,26+1) if not f1(s,2) and f1(s,4)])}')

