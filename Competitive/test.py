def search(arr,left,right,item):
    if (left <= right):
        mid = left  + (right-left)//2
        if (arr[mid] == item):
            return mid
        if(arr[left] <= arr[mid]):
                if(arr[left]<= item and arr[mid]>=item):
                        return search(arr,left,mid-1,item)
                else:
                        search(arr,mid+1,right,item)
        else:
                if(arr[mid]<=item and arr[right]>=item):
                        return search(arr,mid+1,right,item)
                else:
                        return search(arr,left,mid-1,item)
    else:
        return -1
    

arr=[7,8,9,0,1,2,3,4,5,6]
print(search(arr,0,len(arr)-1,9))