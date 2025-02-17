from fnmatch import *
for i in range(0,10**10,3147):
    if fnmatch(str(i),'1*4302?1'): print(i)