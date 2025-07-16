def parition(arr,l,r):
    pvloc=arr[l]
    i,j = l+1,r
    while i<=r:
        while i<r and pvloc > arr[i]:
            i+=1
        while j>=0 and pvloc < arr[j]:
            j-=1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
        else:
            i+=1
    arr[l],arr[j]=arr[j],arr[l]
    return j

def quickSort(arr,l,r):
    if l>=r:
        return
    pivot = parition(arr,l,r)
    quickSort(arr,l,pivot-1)
    quickSort(arr,pivot+1,r)

arr = [9,4,5,6,3,1,1]
quickSort(arr,0,len(arr)-1)
print(arr)