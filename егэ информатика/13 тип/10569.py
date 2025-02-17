from ipaddress import *

net = ip_network(f'10.8.248.131/255.255.224.0',False)
for ip in net:
    print(ip)
    break