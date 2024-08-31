def paid_candy(n,arr,m):
    total_candy=0
    arr.sort()
    for i in arr:
        if( i%5 == 0):
            total_candy += 1
        else:
            if(i <= m):
                m -= i
                total_candy += 1
    return total_candy


n=3
arr=[5,15,105]
m=8

print(paid_candy(n,arr,m))
print(paid_candy(4,[5,4,15,6],5))