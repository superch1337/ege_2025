a = {0:"A",1:"O",2:"Y"}
count = 0
for one in range(3):
    for two in range(3):
        for three in range(3):
            for four in range(3):
                for five in range(3):
                    count += 1
                    if one == 2:
                        print(count)