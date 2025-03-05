for a in range(1,1000):
    count = 0
    for x in range(1,4000):
        if ((a% 7 ==0) and (240 % x == 0) <= ((a % x != 0) <= (780 % x != 0))):
            count += 1
    if count == 3999:
        print(a)
        break