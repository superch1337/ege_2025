print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not((x == (not y)) <= ((z<=(not w)) and (w <= y))):
                    print(x, y, z, w)
                    НЕ РЕШИЛ