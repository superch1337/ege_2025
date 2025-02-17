from fnmatch import fnmatch
for i in range(0,10**8,1991):
    if fnmatch(str(i),'3?1*57'):print(i, i//1991)