arr = [int(i) for i in open("F:\\foege\\17.txt")]
ans = []
ans2 = []
max_el = []
for maxi in arr:
    if len(str(abs(maxi))) == 5 and abs(maxi) % 100 == 43:
        max_el.append(maxi)
maxi = max(max_el)**2
for i in range(len(arr)-2):
    temparr = [arr[i], arr[i+1],arr[i+2]]
    predicate1 = []
    predicate2 = 0
    for d in range(0,2+1):
        if len(str(abs(temparr[d]))) == 5 and abs(temparr[d])%100 == 43:
            predicate1.append(1)
    asum = temparr[0]**2 + temparr[1]**2 + temparr[2]**2
    if asum < maxi:
        predicate2 = 1
    if len(predicate1) >=1 and predicate2 == 1:
        ans.append(asum)
print(len(ans),min(ans))




