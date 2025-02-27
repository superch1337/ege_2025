arr = [int(i) for i in open('17.txt')]
maxx = 0
for i in arr:
    if i > maxx and i%100 == 13:
        maxx = i
ans = []
for i in range(len(arr)-2):
    temp = [arr[i],arr[i+1],arr[i+2]]
    predicate = sum(temp) <= maxx
    predicate2 = len([i for i in temp if len(str(i)) == 3]) == 2
    if predicate and predicate2:
        ans.append(sum(temp))

print(len(ans),max(ans))