def proiz(t):
    result = 1
    for i in t:
        result *= i
    return result
arr = [int(i) for i in open("D:\\foege\\17.txt")]
ans = []
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        temparr = [arr[i], arr[j]]
        predicate = proiz(temparr) % 10 == 0
        if predicate:
            ans.append(sum(temparr))
print(len(ans),max(ans))