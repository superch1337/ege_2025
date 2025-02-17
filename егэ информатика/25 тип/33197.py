
for i in range(1000000,2000000+1):
    count = 0
    for f in range(1,int(i**0.5)):
        if i % f == 0:
            if ((i//f) - f) <= 100:
                count += 1
    if count >= 3: print(i)