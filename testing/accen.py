
def ansR(arr,r,unit):
    if (len(arr) == 0):
        return -1
    else:
        total=r*unit
        sum=0
        # count=0
        for i in range(len(arr)):
            sum+=arr[i]
            # print(sum)
            if sum>= total:
                return i+1
            # count+=1
        return 0



arr=list(map(int,input().split()))
r=7
unit=2
print(ansR(arr,r,unit))