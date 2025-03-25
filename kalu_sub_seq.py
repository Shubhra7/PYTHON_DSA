def generate_subseq(ind,arr,ds,ans):
    if ind==len(arr):
        ans.append(ds[:])
        return
    ds.append(arr[ind])
    generate_subseq(ind+1,arr,ds,ans)
    ds.pop()
    generate_subseq(ind+1,arr,ds,ans)
    

arr=[1,2,3]
ans=[]
ds=[]
generate_subseq(0,arr,ds,ans)
print(ans)
