def search(arr,left,right,item):
    if(left > right):
        return -1
    mid = left + (right - left)//2
    if(arr[mid]==item):
        return mid
    if(arr[left] <= arr[mid]):
        if(arr[left]<=item and item<=arr[mid]):
            return search(arr,left,mid-1,item)
        else:
            return search(arr,mid+1,right,item)
    else:
        if(arr[mid]<=item and item<=arr[right]):
            return search(arr,mid+1,right,item)
        else:
            return search(arr,left,mid-1,item)


arr=[7,8,9,0,1,2,3,4,5,6]
print(search(arr,0,len(arr)-1,9))
print(search(arr,0,len(arr)-1,0))
print(search(arr,0,len(arr)-1,1))
print(search(arr,0,len(arr)-1,2))
print(search(arr,0,len(arr)-1,3))
print(search(arr,0,len(arr)-1,4))
print(search(arr,0,len(arr)-1,5))
print(search(arr,0,len(arr)-1,6))
print(search(arr,0,len(arr)-1,68))