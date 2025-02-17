def f(x,h):
    if x >=102:return h%2 == 0 # меняем только 102 на выигрышное число
    if h == 0: return 0
    listH = [f(x+1,h -1), f(x*2, h-1)]
    return any(listH) if (h-1)% 2 == 0 else any(listH) #при любом это all при неудачном any, только последнее меняем
print(f'19. {min([s for s in range(1,100 +1) if not f(s,1) and f(s, 2)])}')