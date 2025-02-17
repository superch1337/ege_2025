arr = [int(i) for i in open("F:\\foege\\17.txt")]
ans = []
for i in range(len(arr)-1):
    temp = [arr[i],arr[i+1]]
    predicate = sum(temp) % 7 == 0
    predicate2 = temp[0]*temp[1] % 15 == 0
    if predicate and predicate2:
        ans.append(sum(temp))
print(len(ans),max(ans))