count = 0
a = {0:'У', 1:'Ч', 2:'Е', 3:'Н', 4:'И', 5:'К'}
for one in range(6):
    for two in range(6):
        for tree in range(6):
            for four in range(6):
                for five in range(6):
                    if one == 0 and five == 5: count +=1
print(count)