
def cal(arr):
    eve=[]
    odd=[]
    for i in range(len(arr)):
        if (i%2==0):
            eve.append(arr[i])
        else:
            odd.append(arr[i])
    eve.sort()
    odd.sort()
    return(eve[-2] + odd[-2])


arr=[3,4,1,7,9]
print(cal(arr))