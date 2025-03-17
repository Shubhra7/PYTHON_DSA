def find_hcf(n,m):
    while m!=0:
        m,n=n%m,m
    return n

n,m=0,0
print(find_hcf(n,m))
