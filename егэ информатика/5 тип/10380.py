ans = []
for i in range(1000,10000):
    s1 = int(str(i)[0]) + int(str(i)[1])
    s2 = int(str(i)[1]) + int(str(i)[2])
    s3 = int(str(i)[2]) + int(str(i)[3])
    sus = sorted([s1,s2,s3])
    sus.pop(0)
    if f'{sus[0]}{sus[1]}' == '1517':
        ans.append(i)
print(max(ans))