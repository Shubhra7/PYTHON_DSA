
def tar_mes(n):
    ans = (n//60 + 1)*60
    return ans
def combo(arr):
    d={}
    p=[]
    count=0
    for i in arr:
        tar = tar_mes(i)-i
        if(d.get(tar,0) > 0):
            d[tar] -= 1
            count += 1
            p.append([i,tar])
        else:
            d[i]=d.get(i,0)+1
    print(p)
    print(count)
    return count

arr = [2,58,58,2,60,60]
print(combo(arr))