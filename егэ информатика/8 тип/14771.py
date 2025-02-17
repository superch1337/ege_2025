a = {1:'А',2:'П',3:'Р',4:'С',5: 'У'}
count = 0
for one in range(5):
    for two in range(5):
        for tree in range(5):
            count += 1
            if one == 2:
                print(count)
                break