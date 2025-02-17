def replace(value):
    if value == '0': return '1'
    return '0'


ans = []

for N in range(4, 150):
    b = bin(N)[2:]

    array_N = ' '.join(b).split()

    if len(array_N) % 2 != 0:
        array_N[len(array_N) // 2] = replace(array_N[len(array_N) // 2])
    else:
        array_N[len(array_N) // 2] = replace(array_N[len(array_N) // 2])
        array_N[len(array_N) // 2 - 1] = replace(array_N[len(array_N) // 2 - 1])

    b = ''.join(array_N)

    if int(b, 2) > 100 and int(b, 2) < N: ans.append(N)

print(min(ans))