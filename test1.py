def target(n):
    return (60-(n%60))
    # return ((n//60 + 1)*60)
def find_pair(arr):
    d={}
    count=0
    for i in range(len(arr)):
        print("value: ",arr[i])
        req = target(arr[i]) 
        # req = target(arr[i]) - arr[i]
        if(req in d.keys() and d[req]>0):
            count += 1
            d[req] = d[req]-1
            print(req," ",arr[i])
        else:
            d[arr[i]] = d.get(arr[i],0)+1
        print(d,"  ",count)
    # print(d)
    print(count)
    for i in d:
        if(d[i]>0):
            req = target(i)
            print("Hi: ",req)
            if(req in d.keys() and d[req]>0):
                count += 1
                d[req]=d[req]-1
            print(d)
    print(count)
    print(d)


arr=[0,60,58,62,92,88]
print(find_pair(arr))