# arr = [int(i) for i in open("D:\\foege\\17.txt")]
# temps = [i for i in arr if i % 2 == 0]
# srznach = sum(temps) / len(temps)
# tempans = []
# for i in range(0, len(arr) - 1):
#      temploh = [arr[i], arr[i+1]]
#      predicate3 = len([i for i in temploh if i % 3 == 0 and arr[i+1] >= srznach]) == 1
#      predicatesr = len([i for i in temploh if i % 3 != 0 and i < srznach]) == 1
#      if predicatesr and predicate3:
#          tempans.append(sum(tempans))
# print(len(tempans), max(tempans))