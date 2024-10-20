def solve(arr,h):
    low=1
    high=max(arr)
    while(low<=high):
        mid = low +(high -low)//2
        req=0
        for i in arr:
            req += (i//mid) + (i%mid!=0)
        if(req <=h):
            ans=mid
            high=mid-1
        else:
            low = mid+1
    return ans

arr=[4,9,11,17]
h=8

print(solve(arr,h))