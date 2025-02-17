from ipaddress import *

for m in range(33):
    net1 = ip_network(f'165.112.200.70/{m}',False)
    net2 = ip_network(f'165.112.175.80/{m}',False)
    if net1 == net2:
        print(net1)