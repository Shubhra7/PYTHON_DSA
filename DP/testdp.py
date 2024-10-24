# cook your dish here
import sys

def swap(ind,arr):
    temp=arr[ind]
    arr[ind] = arr[-1]
    arr[-1]=temp

def solve(ind,arr,n,mini):
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
        mini = val
        print(mini)
        
    solve(ind+1,arr,n,mini)
    if flag==1:
        swap(ind,arr)
        solve(ind+1,arr,n,mini)
    

t = int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    mini  = sys.maxsize
    solve(0,arr,n,mini)
    print(mini)
