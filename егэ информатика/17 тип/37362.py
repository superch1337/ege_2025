arr = [int(i) for i in open("D:\\foege\\17.txt")]
ass = []
for i in range(len(arr)-1):
    for j in range(i + 1,len(arr)):
        tempfuck = [arr[i], arr[j]]
        predicate1 = sum(tempfuck) % 80 == 0
        predicate2 = len([i for i in tempfuck if i % 50 == 0]) >= 1
        if predicate2 and predicate1:
            ass.append(sum(tempfuck))
print(len(ass), max(ass))

