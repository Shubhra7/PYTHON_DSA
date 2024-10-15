def min_hour_consume(arr,h):
    low=1
    high=max(arr)
    while(low<=high):
        mid = low + (high-low)//2
        req=0
        for i in range(len(arr)):
            req += (arr[i]//mid) + (arr[i]%mid != 0)
        if req<=h:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans



arr = [4,9,11,17]

h=8

ans = min_hour_consume(arr,h)
print(ans)