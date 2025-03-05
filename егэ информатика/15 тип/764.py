for a in range(1,100):
    count = 0
    for x in range(1,1000):
        if (((x % 15 == 0) and (x % 21 != 0)) <= ((x%a != 0) or (x % 15))):
            count += 1
    if count == 999:
        print(a)
        break