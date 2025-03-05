for a in range(0,100):
    count = 0
    for x in range(0,1000):
        if ((x & 107 == 0) <= ((x & 55 != 0) <= (x & a !=0 ))):
            count += 1
    if count == 1000:
        print(a)
        break