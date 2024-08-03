def search(arr,target,left,right):
    if (left > right):
        return -1
    mid = left + (right - left)//2
    if (arr[mid] == target):
        return mid
    if (arr[left] <= arr[mid]):
        kalu.append(1)
        if (arr[left] <= target and arr[mid]>= target):
            return search(arr,target,left,mid-1)
        else:
            return search(arr,target,mid+1,right)
    else:
        golu.append(1)
        if (arr[mid]<=target and arr[right]>=target):
            return search(arr,target,mid+1,right)
        else:
            return search(arr,target,left,mid-1)



kalu=[]
golu=[]
# arr = [10,11,0,1,2,6,9]
# print(search(arr,11,0,len(arr)-1))
# print(search(arr,2,0,len(arr)-1))
arr=[7,8,9,0,1,2,3,4,5,6]
print(search(arr,9,0,len(arr)-1))
print(kalu)
print(golu)