arr = [int(i) for i in open("D:\\foege\\17 (2).txt")]
ans = []
min_el = min(arr)
for i in range(len(arr)-1):
    temp = [arr[i], arr[i+1]]
    if temp[0] % 18 + temp[1] % 18 == min_el: ans.append(sum(temp))
print(len(ans), max(ans))
