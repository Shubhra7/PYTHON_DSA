def best(arr):
    mini=arr[0]
    maxival=0
    for i in range(1,len(arr)):
        val = arr[i]-mini
        if(val > maxival):
            maxival = val
        mini = min(mini,arr[i])
    return maxival

arr = [7,1,5,3,6,4]
print(best(arr))