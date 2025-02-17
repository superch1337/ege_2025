for x in '0123456789AB':
    for y in '0123456789AB':
        tmp = int(f'{y}AA{x}',12) + int(f'{x}02{y}',14)
        if tmp % 80 == 0:
            print(tmp//80)