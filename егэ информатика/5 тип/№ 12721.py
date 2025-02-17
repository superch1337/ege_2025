for n in range(1000):
    o = oct(n)[2::]
    print(n, o)
    o_1 = int(o, 10)
    counter_ch = 0
    while o_1 > 0:
        if o_1 % 2 == 0:
            counter_ch += 1
        o_1 = o_1 // 10
    if counter_ch % 2 == 0:
        o = o[-3::] + '46'
    else:
        o =  o + str((n % 8)*5)
    print(o)