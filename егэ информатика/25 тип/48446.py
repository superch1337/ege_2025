from fnmatch import fnmatch
for i in range(0,10**10,2023):
    if fnmatch(str(i), '1?493*41'): print(i)