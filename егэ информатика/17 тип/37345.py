arr = [int(i) for i in open("F:\\foege\\17 (3).txt")]
ans = []
for i in range(len(arr)-1):
    for j in range(i + 1, len(arr)):
        temp = [arr[i],arr[j]]
        if (temp[0]*temp[1])%62 == 0:
            ans.append(sum(temp))
print(len(ans),max(ans))