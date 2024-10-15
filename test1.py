txt = "BGGBGBBG"
arr = list(txt)
t=2
for i in range(t):
    j=0
    while (j<len(arr)-1):
        if(arr[j]=='B' and arr[j+1]=='G'):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j += 2
        else:
            j+=1

print("".join(arr))