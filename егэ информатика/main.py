#15124
# print('x y z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not((x == y) or ((y or z) <= x)):
#                 print(x,y,z)

# #16809
# for n in range(255+1):
#     b = bin(n)[2:]
#     b = b.zfill(8)
#     b = b.replace('0','2')
#     b = b.replace('1','0')
#     b = b.replace('2','1')
#     res = int(b,2)
#     res -= n
#     if res == 133:
#         print(n)


# 7667
# from itertools import product
# count = 0
# for word in product('ЕГЭ', repeat = 5):
#     if word[0] == 'Г':count +=1
# print(count)

# 5302
# print(15*8 - 10*3)

#15109
# stroka = 77*'1'
# while '11' in stroka:
#     if '222' in stroka: stroka = stroka.replace('222','1',1)
#     else: stroka = stroka.replace('11','2',1)
# print(stroka)

# 3541
# from ipaddress import *
# for mask in range(33):
#     net = ip_network(f'0.0.0.0/{mask}')
#     print(net,net.netmask)

# print(str(4**255 + 2**255 - 255).count('1'))

# # 6958
# def f(n):
#     if n == 1: return 1
#     if n > 1: return f(n-1) + n
# print(f(30))

#46977
# def f(x,h):
#     if x >= 21: return h % 2 == 0
#     if h == 0: return 0
#     listH = [f(x+1,h-1),f(x+2,h-1),f(x*2,h-1)]
#
#     return any(listH) if(h-1)%2 == 0 else all(listH)
# print(f'19. {min([s for s in range(1,20+1) if not f(s,1) and f(s,2)])}')

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((x and (not(y))) <= ((not(z) or (not(w)))) and ((w <= x) or y)):
#                     print(x,y,z,w)

# ans = []
# for n in range(100,1000):
#     s1 = int(str(n)[0]) + int(str(n)[1])
#     s2 = int(str(n)[1]) + int(str(n)[2])
#     res = ''
#     if s1 > s2: res = f'{s2}{s1}'
#     else: res = f'{s1}{s2}'
#     if res == '1216':
#         ans.append(n)
# print(len(ans))

# print(max(bin(int('010',2)),bin(int('011',2))))
# print(320*640*8/8/1024)

# from itertools import product
# count = 0
# for word in product('УОА', repeat = 6):
#     count += 1
#     word = ''.join(word)
#     if  word == 'ОУУУОО':
#         print(count)
#         break


# b = bin(80)[2:]
# b2 = bin(12)[2:]
# print((len(b) + len(b2) + 14*6)/8)

# from random import shuffle
# for i in range(50):
#     s = list('1'*12+'2'*15+'3'*17)
#     shuffle(s)
#     s = '0' + ''.join(s)
#     while '01' in s or '02' in s or '03' in s:
#         s = s.replace('01','103',1)
#         s = s.replace('02','10',1)
#         s = s.replace('03','210',1)
#     print(s.count('2'))

# a = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')[:10]
# for x in a:
#     tmp = int(f'28{x}2',18) + int(f'93{x}5',12)
#     if tmp % 133 == 0:
#         print(tmp//133)

# def f(n):
#     if n < 9: return n
#     else: return f(n%9) + f(n//9)
# count = 0
# for i in range(4*6**20,5*6**20+1):
#     if f(i) == 121: count += 1
# print(count)

# def f(x,y):
#     if x == y: return 1
#     if x > y: return 0
#     else: return f(x+2,y) + f(x+5,y)
# print(f(1,20))

# from fnmatch import fnmatch
#
# for i in range(0,10**10,2024):
#     if fnmatch(str(i),'1?2157*4'): print(i, i//2024)

# def f(x,h):
#     if x >= 38: return h%2 == 0
#     if h == 0: return 0
#     listH = [f(x+1,h-1),f(x*3,h-1)]
#     return any(listH) if(h-1)%2 == 0 else all(listH)
# print(f'19. {min([s for s in range(1,37+1)if not f(s,1) and f(s,2)])}')
# print(f'20. {[s for s in range(1,37+1) if not f(s,1) and f(s, 3)]}')
# print(f'21. {[s for s in range(1,37+1) if not f(s,2) and f(s, 4)]}')

# from turtle import *
# width(1)
# lt(90)
# tracer(0)
# a = 20
#
# for i in range(4):
#     fd(6*a)
#     rt(150)
#     fd(6*a)
#     rt(30)
# up()
# for x in range(20,-20,-1):
#     for y in range(20,-20,-1):
#         goto(x*a,y*a)
#         dot(3, 'red')
#
# down()
# done()

print(180*4*120)