def permut(ind,arr,ans):
    if ind==len(arr)-1:
        ans.append("".join(arr))
        return
    for i in range(ind,len(arr)):
        arr[i],arr[ind]=arr[ind],arr[i]
        permut(ind+1,arr,ans)
        arr[i],arr[ind]=arr[ind],arr[i]
    


s = "ABC"
ans=[]
arr=list(s)
permut(0,arr,ans)
print(ans)