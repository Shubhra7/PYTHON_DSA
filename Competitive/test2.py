import sys
def min_hour_consume(arr,h):
    low=1
    high=max(arr)
    ans=sys.maxsize
    while(low<=high):
        mid = low + (high-low)//2
        req=0
        for i in arr:
            req += (i//mid) + (i%mid!=0)
        print(mid," : ",req)
        if req <= h:
            ans=mid
            high=mid-1
            print("Yes")
        else:
            low = mid+1
    return ans

arr = [4,9,11,17]

h=8

ans = min_hour_consume(arr,h)
print(ans)

