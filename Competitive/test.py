def diffof(n,m):
    div=[]
    nondiv=[]
    for i in range(1,m+1):
        if (i%n == 0):
            div.append(i)
        else:
            nondiv.append(i)
    return abs(sum(nondiv) - sum(div))



print(diffof(3,10))
print(diffof(4,20))