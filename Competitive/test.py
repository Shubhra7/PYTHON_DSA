def modified_bin(arr,target,left,right):
    if (left > right):
        return -1
    mid = left + (right - left)//2
    if (arr[mid] == target):
        return mid
    elif (arr[left] <= arr[mid-1]):
        print("hi1")
        if (arr[left]>=target and arr[mid -1]>=target):
            return modified_bin(arr,target,left,mid-1)
        else:
            return modified_bin(arr,target,mid+1,right)
    else:
        print("hi1")        
        if (arr[mid+1]>=target and arr[right]>=target):
            return modified_bin(arr,target,mid+1,right)
        else:
            return modified_bin(arr,target,left,mid-1)
    

def search(arr,target):
    return modified_bin(arr,target,0,len(arr)-1)


arr=[7,8,9,0,1,2,3,4,5,6]
print(search(arr,8))
print(search(arr,2))