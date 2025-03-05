for a in range(1,100):
    count = 0
    for x in range(1,1000):
        if (((x % 4 != 3) or (x % 6 != 1)) <= (x% 36 != a)):
            count += 1
    if count == 999:
        print(a)
        break