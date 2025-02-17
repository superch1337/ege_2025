arr = [int(i) for i in open("F:\\foege\\171.txt")]
ans = []
kol = len([i for i in arr if i % 32 == 0])
for i in range(len(arr)-1):
    temp = [arr[i], arr[i+1]]
    predicate1 = temp[0] < 0 or temp[1] < 0
    predicate2 = (sum(temp)) < kol
    if predicate1 and predicate2:
        ans.append(sum(temp))
print(max(ans),len(ans))