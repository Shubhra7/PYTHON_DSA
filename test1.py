def paid_candy(n,arr,m):
    count=0
    for i in range(n):
        if(arr[i]%5 == 0):
            count += 1
        elif(m >= arr[i]):
            m -= arr[i]
            count += 1
    return count

n=3
arr=[5,15,105]
m=8

print(paid_candy(n,arr,m))
print(paid_candy(4,[5,4,15,6],5))
print(paid_candy(4,[5,8,15,6],5))