# https://youtu.be/4lJVQ16HQ-A

"""
You are given a triplet of integer a,b,c. you can perform the following operation
any number of times.

select any two numbers from the triplet
add 1 to both selected numbers
subtract 1 from the remaining number

Your tast is to determine the number of steps needed to maket all three numbers equal
using the given operations.

Input:
3
1 2 3
4 4 4 
2 2 8

Output:
-1 
0 
3
"""
def min_steps(arr):
    arr.sort()
    if arr[0]==arr[1] and arr[1]==arr[2]:
        return 0
    steps=0
    while True:
        arr[0]+=1
        arr[1]+=1
        arr[2]-=1
        steps+=1
        arr.sort()
        if arr[0]==arr[1] and arr[1]==arr[2]:
            return steps
        if (arr[0]==arr[1] and arr[1]+1==arr[2] ) or (arr[1]==arr[2] and arr[0]+1==arr[1]):
            return -1
        


t=int(input())
for _ in range(t):
    arr=list(map(int,input().split()))
    print(min_steps(arr))
