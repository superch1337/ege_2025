# for i in range(1000000,0,-1):
#     if i * 48000 * 2 * 0.16 / 8 / 1024 <= 45:
#         print(i)
#         break

# 3200
# from itertools import product
# count = 0
# for word in product('АОУ',repeat = 5):
#     count += 1
#     if word[0] == 'У':
#         print(count)
#         break

# from random import shuffle
# for i in range(60):
#     for g in range(60):
#         for y in range(60):
#             s = '0' + '1'*i + '2'*g + '3'*y
#             while '01' in s or '02' in s or '03' in s:
#                 s = s.replace('01','30',1)
#                 s = s.replace('02', '101', 1)
#                 s = s.replace('03', '202', 1)
#             if s.count('1') == 15 and s.count('2') == 10 and s.count('3') == 60:
#                 print(i)
#                 break

# from ipaddress import *
# for mask in range(33):
#     net = ip_network(f'203.155.196.98/{mask}',False)
#     print(net)

# print(bin(4**14+2**32-4)[2:].count('1'))

# from sys import *
# setrecursionlimit(10**8)
# def f(n):
#     if n < 3: return 2
#     if n > 2 and n % 2 == 0: return f(n-2)+f(n-1)-n
#     else: return f(n-1)-f(n-2)+2*n
# print(f(32))

# for a in range(0,100):
#     count = 0
#     for x in range(0,300):
#         for y in range(0,300):
#             if ((2*x+3*y != 60) or (a>=x) or (a>=y)):
#                 count += 1
#     if count == 90000:
#         print(a)
#         break

arr = [int(i) for i in open('171.txt')]
ans = []
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        tmp = [arr[i],arr[j]]
        if (abs(tmp[0] - tmp[1]) % 2 == 0) and (tmp[0] % 19 == 0 or tmp[1] % 19 == 0):
            ans.append(sum(tmp))
print(len(ans),max(ans))


# def f(x,y,d):
#     if x == y: return 1
#     if x > y: return 0
#     else:
#         if d == 'a': return f(x+1,y,'c') + f(x+2,y,'b')
#         else: return f(x+1,y,'c') + f(x+2,y,'b') + f(x*2,y,'a')
#
#
# print(f(1,11,''))