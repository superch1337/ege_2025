arr = [int(i) for i in open("D:\\foege\\17.txt")]
ans = []
max_el = max([i for i in arr if i % 1000 == 832])
for i in range(len(arr) - 2):
    temp = [arr[i], arr[i+1], arr[i+2]]
    predicate1 = 0 < (len([i for i in temp if len(str(abs(i))) == 4])) < 3
    predicate2 = (len([i for i in temp if i % 5 == 0])) > (len([i for i in temp if i % 3 == 0]))
    predicate3 = (sum(temp)) > max_el
    if predicate1 and predicate2 and predicate3:
        ans.append(sum(temp))
print(len(ans), max(ans))