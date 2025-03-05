for a in range(0,300):
    count = 0
    for x in range(0,300):
        for y in range(0,300):
            if ((x > 39) or (y > 26) or ((2 * x + 4*y) < a)):
                count += 1
    if count == 90000:
        print(a)
        break