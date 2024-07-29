
def diffof(n,m):
    div=[]
    nodiv=[]
    for i in range(1,m+1):
        if i % n==0:
            div.append(i)
        else:
            nodiv.append(i)
    return abs(sum(div) - sum(nodiv))


n=4
m=20
print(diffof(n,m))
print(diffof(3,10))