a = {0:'В',1:'Е',2:'С',3:'Т'}
count = 0
for one in range(4):
    for two in range(4):
        for tree in range(4):
            for four in range(4):
                for five in range(4):
                    for six in range(4):
                        count += 1
                        if one == 3:
                            print(count)
                            break


