arr = [int(i) for i in open("D:\\foege\\17.txt")]
ans = []
max_el = max([i for i in arr if abs(i) % 100 == 13])
for i in range(len(arr) - 2):
    temp1 = [arr[i], arr[i+1], arr[i+2]]
    predicate1 = len([i for i in temp1 if len(str(abs(i))) == 3]) == 2
    predicate2 = sum(temp1) < max_el
    if predicate1 and predicate2:
        ans.append(sum(temp1))
print(len(ans), min(ans))