# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import copy
def all_seq(ind,arr,dp,ans):
    if ind==len(arr):
        ans.append(copy.deepcopy(dp))
        return ans
    dp.append(arr[ind])
    all_seq(ind+1,arr,dp,ans)
    dp.pop()
    all_seq(ind+1,arr,dp,ans)
    
    

print("Try programiz.pro")
arr=[2,3,4]
dp=[]
ans=[]
all_seq(0,arr,dp,ans)
print(ans)
