for num in range(185311,185330+1):
    list_del = []
    for i in range(1,num+1):
        if num % i == 0: list_del.append(i)
        if len(list_del) > 4: break
    if len(list_del) == 4: print(list_del)
