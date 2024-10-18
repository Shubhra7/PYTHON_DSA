import copy 

def find_seq(ind,arr,ds,ans,target):
    if(ind == len(arr)):
        if(target == 0):
                ans.append(copy.deepcopy(ds))
        return
    if(target >= arr[ind]):
        ds.append(arr[ind])
        find_seq(ind,arr,ds,ans,target-arr[ind])
        ds.pop()
    find_seq(ind+1,arr,ds,ans,target)
    

# arr = [3,2,1]
arr = [2,3,6,7]
ds=[]
ans=[]
target=7
find_seq(0,arr,ds,ans,target)
print("The possible sub sequences are: ",ans)