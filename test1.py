arr=[1,2,3,4,5,6,7]
k=3
arr=arr[::-1]

i,j = 0,k-1
while i<j:
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    i+=1
    j-=1

i,j = k,len(arr)-1
while i<j:
    temp = arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    i+=1
    j-=1

print(arr)