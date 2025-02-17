arr = [int(i) for i in open("D:\\foege\\17 (2).txt")]
ans = []
def razn(t): tilt = t[0] - t[1]; return tilt
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        temp = [arr[i], arr[j]]
        predicate1 = razn(temp) % 80 == 0
        if predicate1:
            ans.append(razn(temp))
print(len(ans), max(ans))