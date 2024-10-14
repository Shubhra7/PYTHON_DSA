text = "hello.my.name.is.shauraya"
arr = text.split('.')

ans=''
maxi=0
for i in range(len(arr)):
    if(len(arr[i]) > maxi):
        ans=arr[i]
        maxi = len(arr[i])

print(ans)
print(maxi)
