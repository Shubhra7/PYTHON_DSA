# cook your dish here
import sys
import copy
def swap(ind,arr):
    temp=arr[ind]
    arr[ind] = arr[-1]
    arr[-1]=temp

def solve(ind,arr,n,mini,minarr):
    flag=0
    if(ind == n):
        return
    if(arr[ind] <= (2*arr[n])):
        flag=1
        swap(ind,arr)
    print(arr)
    val = sum(arr[:n])
    print(val)
    if( mini > val):
        mini = copy.deepcopy(val)
        minarr.append(copy.deepcopy(val))
        print("HI: ",mini)
        
    solve(ind+1,arr,n,mini,minarr)
    if flag==1:
        swap(ind,arr)
        solve(ind+1,arr,n,mini,minarr)
    

t = int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    mini  = sys.maxsize
    minarr=[]
    solve(0,arr,n,mini,minarr)
    print(mini)
    print(minarr)
