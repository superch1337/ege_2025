
for num in range(95632,95700+1):
    spisdel = []
    for i in range(2,num+1,2):
        if num % i == 0: spisdel.append(i)
        if len(spisdel) > 6:
            break
    if len(spisdel) == 6:
        print(spisdel)