for a in range(1,100):
    count = 0
    for x in range(1,1000):
        if (((x % a == 0) and (x% 24 ==0) and(x % 16 != 0)) <= (x % a != 0)):
            count += 1
    if count == 999:
        print(a)
        break
