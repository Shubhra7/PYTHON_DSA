
def lgsm(arr):
    if (len(arr) == 0):
        return 0
    else:
        eve=[]
        odd=[]
        for i in range(len(arr)):
            if i%2==0:
                eve.append(arr[i])
            else:
                odd.append(arr[i])
        eve.sort()
        odd.sort()
        ans= eve[-2] + odd[1]
        return ans

arr=list(map(int,input().split()))
print(lgsm(arr))