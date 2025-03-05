for a in range(100,0,-1):
    count = 0
    for x in range(0,1000):
        if ((((x & 13 != 0) or (x & a != 0)) <= (x & 13 != 0)) or ((x & a != 0) and (x & 39 == 0))):
            count += 1
    if count == 1000:
        print(a)
        break