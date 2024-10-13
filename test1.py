import copy
def find_seq(ind,arr,ds,ans,target):
    # if(ind == len(arr)):
    if(target < 0 ):
        if(sum(ds)==target):
            ans.append(copy.deepcopy(ds))
            print(ds)
        return
    ds.append(arr[ind])
    find_seq(ind,arr,ds,ans,target-arr[ind])
    ds.pop()
    find_seq(ind+1,arr,ds,ans,target-arr[ind])
arr = [3,2,1]
ds=[]
ans=[]
target = 6
find_seq(0,arr,ds,ans,target)
print(ans)