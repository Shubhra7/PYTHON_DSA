import sys

def frogJump(n, heights) -> int:

    # Write your code here.
    prev, prev2=0,0
    for i in range(1,len(arr)):
        ls = prev + abs(heights[i] - heights[i-1])
        rs=sys.maxsize
        if i>1:
            rs = prev2 + abs(heights[i] - heights[i-2])
        prev2 = prev
        prev = min(ls,rs)
    return prev

# arr=[10,20,30,10]
arr=[10,50,10]
print(frogJump(len(arr),arr))