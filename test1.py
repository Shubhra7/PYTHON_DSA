arr=[1,2,3,4,5,6,7]
k=1
arr = arr[::-1]

i=0
j=k-1
while( i<j):
    arr[j] = arr[i] ^ arr[j]
    arr[i] = arr[i] ^ arr[j]
    arr[j] = arr[i] ^ arr[j]
    i+=1
    j -=1

i=k
j=len(arr)-1
while( i<j):
    arr[j] = arr[i] ^ arr[j]
    arr[i] = arr[i] ^ arr[j]
    arr[j] = arr[i] ^ arr[j]
    i+=1
    j -=1
print(arr)