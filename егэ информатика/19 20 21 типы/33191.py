def f(x,y,h):
    if x + y >= 91: return h % 2 == 0
    if h == 0: return 0
    listH = [f(x+1,y,h -1), f(x,y+1,h-1),f(x,y*4,h-1), f(x*4,y,h-1)]
    return any(listH) if (h -1)% 2  == 0 else any(listH)
def f1(x,y,h):
    if x + y >= 91: return h % 2 == 0
    if h == 0: return 0
    listH = [f1(x+1,y,h -1), f1(x,y+1,h-1),f1(x,y*4,h-1), f1(x*4,y,h-1)]
    return any(listH) if (h -1)% 2  == 0 else all(listH)
print(f'19. {min([s for s in range(1,84 + 1) if not f(5,s,1) and f(5, s, 2)])}')
print(f'20. {([s for s in range (1,84+1) if not f1(5, s, 1) and f1(5,s,3)])}')
print(f'21. {min([s for s in range(1,84+1) if not f1(5,s,2) and f1(5,s,4)])}')