import copy
def find_seq(ind,arr,ds,ans):
    if(ind == len(arr)):
        ans.append(copy.deepcopy(ds))
        return
    ds.append(arr[ind])
    find_seq(ind+1,arr,ds,ans)
    ds.pop()
    find_seq(ind+1,arr,ds,ans)
arr=[1,2,3]
ds=[]
ans=[]
find_seq(0,arr,ds,ans)
print("The sub sequences are: ",ans)