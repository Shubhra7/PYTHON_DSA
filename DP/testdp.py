def permu(ind,arr,ds,ans):
    if ind == len(arr):
        ans.append(ds[:])
    for i in range(ind,len(arr)):
        ds.append(arr[i])
        arr[i],arr[ind] = arr[ind],arr[i]
        permu(ind+1,arr,ds,ans)
        ds.pop()
        arr[i],arr[ind] = arr[ind],arr[i]

arr=[1,2,3,4]
ds=[]
ans=[]
permu(0,arr,ds,ans)
print(ans)
print(len(ans))