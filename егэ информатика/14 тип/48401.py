for x in '0123456789ABC':
    tmp = int(f'{x}A04',13) + int(f'1D{x}3',18)
    if tmp % 184 == 0: print(tmp//184)