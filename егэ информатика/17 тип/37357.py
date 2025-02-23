arr = [int(i) for i in open('17.txt')]
ans = []
for i in range(len(arr)-1):
    temp = [arr[i],arr[i+1]]
    predicate = sum(temp) % 8 ==0
    if predicate:
        ans.append(sum(temp))
print(len(ans),max(ans))
