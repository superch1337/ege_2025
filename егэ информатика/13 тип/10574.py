from ipaddress import *
count = 0
for m in range(33):
    net = ip_network(f'158.116.11.146/{m}',False)
    if '158.116.0.0' in str(net):
            count += 1
print(count)