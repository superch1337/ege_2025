a = {0:"К",1:"Л",2:"Н",3:"Т",4:"Э"}
count = 0
for one in range(5):
    for two in range(5):
        for three in range(5):
            for four in range(5):
                for five in range(5):
                    for six in range(5):
                        count += 1
                        if one == 0 and two == 0 and three == 1 and four == 0 and five == 1 and six == 0:
                            print(count)
                            break