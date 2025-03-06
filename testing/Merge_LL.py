def canArrange(arr,k):
    ans=[]
    d={}
    for i in range(len(arr)):
        rem=arr[i]%k
        if (k-rem) in d:
            ans.append([arr[i],d[k-rem]])
        d[rem]=arr[i]
    return ans


print(canArrange([1,2,3,4,5,10,6,7,8,9],5))