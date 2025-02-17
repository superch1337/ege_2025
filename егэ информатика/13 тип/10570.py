from ipaddress import *
for m in range(33):
    net = ip_network(f'122.21.49.91/{m}',False)
    print(net)


