from ipaddress import *
ans = []
for m in range(33):
    net = ip_network(f'191.173.145.240/{m}',False)
    if '191.173.144.0' in str(net):ans.append(net.num_addresses)
print(min(ans))

print(min([ip_network(f'191.173.145.240/{m}', False).num_addresses for m in range(33) if '191.173.144.0' in str(ip_network(f'191.173.145.240/{m}', False))]))