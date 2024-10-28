def target(n):
    ans = ((n//60)+1)*60
    return ans

arr = [2,58,58,2,60,60]
d={}
count=0
for i in range(len(arr)):
    tar = target(arr[i]) - arr[i]
    if(tar in d and d[tar]>0):
        d[tar]-=1
        count += 1
        print(arr[i]," ",tar)
    else:
        d[arr[i]] = d.get(arr[i],0)+1 
print(count)
