import copy

def find_subseq(index,arr,ds,ans,sumans):
    if(index == len(arr)):
        ans.append(copy.deepcopy(ds))
        sumans.append(sum(ds))
        return
    ds.append(arr[index])
    find_subseq(index+1,arr,ds,ans,sumans)
    ds.pop()
    find_subseq(index+1,arr,ds,ans,sumans)

arr=[1,2,3]
ds=[]
ans=[]
sumans=[]
find_subseq(0,arr,ds,ans,sumans)
print(ans)
print(sumans)