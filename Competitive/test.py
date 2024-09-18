def target(n):
    ans=((n//60 + 1)*60)
    return ans

arr = [2,58,58,2,60,60]
d={}
l=[]
count=0
for i in range(len(arr)):
    req = target(arr[i]) - arr[i]
    if(req in d.keys() and d[req]>0):
        count += 1
        d[req] -= 1
        l.append([arr[i],req])
    else:
        d[arr[i]] = d.get(arr[i],0)+1
print(count)
print("The pairs are: ")
print(l)


    
