arr = [int(i) for i in open("D:\\foege\\17.txt")]
ans = []
ans2 = []
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        temparr = [arr[i], arr[j]]
        predicate1 = sum(temparr) % 9 == 0
        if predicate1: ans.append(sum(temparr))
print(len(ans),max(ans))