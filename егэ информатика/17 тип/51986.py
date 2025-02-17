arr = [int(i) for i in open("D:\\foege\\17.txt")]
ans = []
temp1= []
temp2 = []
for i in range(len(arr)- 1):
    temp1 = [arr[i], arr[i+1]]
    predicate1 = min(temp1) % 10 == 5
    a = min(temp1) % 10 == 5
    predicate2 = sum(temp1) < a
    if predicate2 and predicate1:
        ans.append(temp1)
    d = temp1[0]**2 + temp1[1]**2
    temp2.append(d)
print(len(temp1),max(temp2))