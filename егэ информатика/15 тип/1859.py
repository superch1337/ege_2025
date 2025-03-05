for a in range(400,0,-1):
    count = 0
    for x in range(0,400):
        for y in range(0,400):
            if (((2 *x + y) != 70) or (x < y) or (a <x)): count += 1
    if count == 160000:
        print(a)
        break
