import copy
def find_subarr(arr,ans,toggles=None,i=0):
    if toggles==None:
        toggles=[0]*len(arr)
    if(i==len(arr)):
        subarr=[arr[i] for i in range(len(arr)) if toggles[i]==1]
        if(sum(subarr) == 2):
            ans.append(copy.deepcopy(subarr))
        return
    toggles[i]=0
    find_subarr(arr,ans,toggles,i+1)
    toggles[i]=1
    find_subarr(arr,ans,toggles,i+1)


arr=[1,0,0,1,1,0]
ans=[]
find_subarr(arr,ans)
print(ans)
print(len(ans))