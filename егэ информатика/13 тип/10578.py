from ipaddress import *

for m in range(33):
    net1 = ip_network(f'10.96.180.231/{m}',False)
    net2 = ip_network(f'10.96.140.118/{m}',False)
    if net1 != net2:
        print(32-m)