def paid_candy(n,arr,m):
    tot = 0
    arr.sort()
    for i in arr:
        if(i%5 == 0):
            tot += 1
        else:
            if(i<m):
                m -= i
                tot += 1
    return tot



print(paid_candy(4,[5,4,15,6],5))
print(paid_candy(4,[5,8,15,6],5))