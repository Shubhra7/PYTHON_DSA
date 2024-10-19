import copy
def find_seq(ind,arr,ds,ans):
    if(ind == len(arr)):
        ans.append(copy.deepcopy(ds))
        return
    ds.append(arr[ind])
    find_seq(ind+1,arr,ds,ans)
    ds.pop()
    find_seq(ind+1,arr,ds,ans)

x="niveditha"
y="lavekdahnita"
s,r = 3,5
ans = []
ds=[]
arr=list(y)
find_seq(0,arr,ds,ans)
print(ans)

rev, stra = 0,0
j=1
i=0
while j<len(x):
    val = x[i:j]
    if(list(val) in ans):
        if((j+1) in range(len(x)) and list(x[i:j+1]) not in ans):
            stra += 1
            i=j
            j += 1
    if(list(val)[::-1] in ans):
        if(j+1 in range(len(x)) and list(x[i:j+1][::-1]) not in ans):
            rev += 1
            i=j
            j += 1

print(stra)
print(rev)

    


