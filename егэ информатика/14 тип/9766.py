def troich(a):
    res = ''
    while a != 0:
        res = str(a%3) + res
        a = a//3
    return res

print(troich(9**8+3**8-2).count("2"))