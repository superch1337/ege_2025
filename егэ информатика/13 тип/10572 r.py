from ipaddress import *
for m in range(33):
    net = ip_network(f'173.103.25.118/{m}', False)
    print(net)