def target(n):
    return ((n//60) +  1)*60

arr = [2,58,58,2,60,60]

d={}
l=[]
count=0
for i in range(len(arr)):
    tar = (target(arr[i]) - arr[i])
    if tar in d and d[tar]>0:
        l.append([arr[i],tar])
        d[tar] -= 1
        count += 1
    else:
        d[tar] = d.get(tar,0)+1
print(d)
print(count)
print(l)
