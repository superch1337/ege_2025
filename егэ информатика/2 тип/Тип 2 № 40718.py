print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(((x <= y) and (z or w)) <= ((x == w) or (y and not(z)))):
                    print(x, y, z, w)
