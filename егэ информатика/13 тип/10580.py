from ipaddress import *
k = 0
net = ip_network(f'10.48.96.0/255.255.240.0',False)
for ip in net:
    b = f'{ip:b}'
    if b.count('1') > b.count('0'):
        k += 1
print(k)