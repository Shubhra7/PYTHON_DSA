def ispalin(s):
    return (str(s) == str(s)[::-1])

arr = list(map(int,input().split()))

arr.sort(reverse=True)

for i in range(len(arr)):
    if(ispalin(arr[i])):
        print("Largest palind: ",arr[i])
        break
else:
    print("Not present")