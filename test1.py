text = "hello.hubhrajit.name.is.shubhrajit"

arr = list(text.split('.'))

maxi=0
ans=""
for i in range(len(arr)):
    if(len(arr[i]) > maxi):
        maxi = len(arr[i])
        ans = arr[i]

print(ans)
