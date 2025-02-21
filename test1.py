import copy
def subseq(ind,arr,ds,ans):
    if ind==len(arr):
        ans.append(copy.deepcopy(ds))
        return
    ds.append(arr[ind])
    subseq(ind+1,arr,ds,ans)
    ds.pop()
    subseq(ind+1,arr,ds,ans)

arr=[10,6,1]
ans=[]
ds=[]
subseq(0,arr,ds,ans)
print(ans)