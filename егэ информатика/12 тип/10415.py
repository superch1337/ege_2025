s = 99*'8' + '1'
while '133' in s or '881' in s:
    if '133' in s: s = s.replace('133','81',1)
    else: s = s.replace('881','13')
print(s)