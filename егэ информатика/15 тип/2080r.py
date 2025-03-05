for a in range(0,300):
    count = 0
    for x in range(0,300):
        for y in range(0,300):
            if (((x**2 - 10*x + 16) >0) or ((y**2 - 10*y +21) > 0) or ((x*y) < 2*a)):
                count += 1
    if count == 90000:
        print(a)
        break