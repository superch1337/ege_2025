from ipaddress import *

for m in range(33):
    net = ip_network(f'118.193.30.139/{m}', 0)
    print(net, net.netmask)

