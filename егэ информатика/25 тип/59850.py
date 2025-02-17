from fnmatch import fnmatch
for i in range(0,10**8, 2622):
    if fnmatch(str(i), '1?4*6?8'): print(i,i//2622)