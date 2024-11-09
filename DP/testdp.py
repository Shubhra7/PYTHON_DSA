def sum_seq(ind,arr,ds,target,s):
    if(ind == len(arr)):
        if(s == target):
            print(ds)
            return True
        return False
    ds.append(arr[ind])
    s += arr[ind]
    if(sum_seq(ind+1,arr,ds,target,s)==True):
        return True
    ds.pop()
    s -= arr[ind]
    if(sum_seq(ind+1,arr,ds,target,s)==True):
        return True
    return False


arr=[1,2,1,1]
target=3
ds=[]
sum_seq(0,arr,ds,target,0)