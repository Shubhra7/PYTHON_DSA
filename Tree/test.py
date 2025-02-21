import copy
def subseq(ind,arr,ds,ans):
    if ind == len(arr):
        if len(ds)==0:
            return
        val=1
        for i in ds:
            val *= i
        # ans.append(copy.deepcopy(ds))
        ans.append(copy.deepcopy(val))
        return
    ds.append(arr[ind])
    subseq(ind+1,arr,ds,ans)
    ds.pop()
    subseq(ind+1,arr,ds,ans)
def isPrime(n):
    if n>1 and n<=3:
        return True
    if ((n**2)-1)%24==0:
        return True
    return False
def check_beau(n):
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            if not isPrime(i):
                return False
    return True
        
arr=[10,6,1]
# arr=[3]
ans=[]
ds=[]
subseq(0,arr,ds,ans)
print("kalu ",ans)
finalans=[]
for i in ans:
    if i!=1:
        if check_beau(i):
            print(i,"---HI")
            finalans.append(i)
print(finalans)
print(len(finalans))