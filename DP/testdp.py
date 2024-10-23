import copy
def seq(ind,arr,ds,ans,s,target):
    if(ind == len(arr)):
        if(target == s):
            ans.append(copy.deepcopy(ds))
            return 1
        return 0
    ds.append(arr[ind])
    s += arr[ind]
    r= seq(ind+1,arr,ds,ans,s,target)
    ds.pop()
    s -= arr[ind]
    l=seq(ind+1,arr,ds,ans,s,target)
    return r+l

arr = [3,2,1]
ds=[]
ans=[]
target=3
s=0
print(seq(0,arr,ds,ans,s,target))
print(ans)