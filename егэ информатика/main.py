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
def f(x,h):
    if x >= 21: return h % 2 == 0
    if h == 0: return 0
    listH = [f(x+1,h-1),f(x+2,h-1),f(x*2,h-1)]

    return any(listH) if(h-1)%2 == 0 else all(listH)
print(f'19. {min([s for s in range(1,20+1) if not f(s,1) and f(s,2)])}')

