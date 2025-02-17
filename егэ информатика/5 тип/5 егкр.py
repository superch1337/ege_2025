from itertools import count


def troich(x):
    res = ''
    while x > 0:
        res = f'{x%3}{res}'
        x = x//3
    return res
ans = []
for n in range(1, 1000):
    t = troich(n)
    if n % 3 == 0:
        t = f'{t}{t[-2:]}'
    if n % 3 != 0:
        a = t.count('1') + 2*t.count('2')
        t += troich(a)
    if int(t,3) > 220 and int(t,3)%2 == 0:
        ans.append(int(t, 3))
print(min(ans))

