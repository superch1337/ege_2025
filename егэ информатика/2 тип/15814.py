print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if ((x == (w and y)) or ((w <= y) and (y <=w))) == 0:
                    print(w,x,y,z)