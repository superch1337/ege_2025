a = {0:'А',1:'И',2:'О',3:'У',4:'Э'}
count = 0
for one in range(5):
    for two in range(5):
        for tree in range(5):
            for four in range(5):
                count += 1
                if one == 1 and two == 0 and tree == 0 and four == 4:print(count)
