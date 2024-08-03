def search(arr,target,left,right):
    if (left > right):
        return -1
    mid = left + (right - left)//2
    if (arr[mid] == target):
        return mid
    if (arr[left] <= arr[mid]):
        if (arr[left] <= target and arr[mid]>= target):
            return search(arr,target,left,mid-1)
        else:
            return search(arr,target,mid+1,right)
    else:
        if (arr[mid]<=target and arr[right]>=target):
            return search(arr,target,mid+1,right)
        else:
            return search(arr,target,left,mid-1)




arr = [10,11,0,1,2,6,9]
print(search(arr,11,0,len(arr)-1))
print(search(arr,2,0,len(arr)-1))