for a in range(0,300):
    count = 0
    for x in range(0,300):
        for y in range(0,300):
            if not(((x*y) > a) and (x > y) and (x < 8)):
                count += 1
    if count == 90000:
        print(a)
        break