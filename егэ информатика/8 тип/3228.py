a = {0: 'А',1:'О',2:'У'}
count = 0
for one in range(0,3):
    for two in range(0, 3):
        for tree in range(0, 3):
            for four in range(0, 3):
                for five in range(0, 3):
                    count += 1
                    if one == 2 and two == 0 and tree == 2 and four == 0 and five == 2:
                        print(count)
