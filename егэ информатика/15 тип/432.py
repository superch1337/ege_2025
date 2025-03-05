for a in range(1,3000):
    count = 0
    for x in range(1,3000):
        if (((x % 84 != 0) or (x % 90 != 0)) <= (x % a != 0)):
            count += 1
    if count == 2999:
        print(a)
        break
