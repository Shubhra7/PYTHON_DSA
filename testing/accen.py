
import sys

def Psu(s,arr):
    if (len(arr) < 2):
        return -1
    else:
        maxi=sys.maxsize
        ans=0
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                val=arr[i] + arr[j]
                if(val<=s):
                    if(maxi > val):
                        maxi=val
                        ans=arr[i]*arr[j]
        return ans



sum=int(input())
arr=list(map(int,input().split()))
print(Psu(sum,arr))