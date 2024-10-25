def val_get(arr,mid):
    count = 0
    for i in range(len(arr)):
        count += (arr[i]//mid) + (arr[i]%mid != 0)
    return count

def min_hour(arr,h):
    low=1
    high=max(arr)
    while low<=high:
        mid = low + (high-low)//2
        val = val_get(arr,mid)
        if( val <= h):
            high = mid-1
            ans=mid
        else:
            low = mid+1
    return ans

arr = [4,9,11,17]
h=8

ans = min_hour(arr,h)
print(ans)