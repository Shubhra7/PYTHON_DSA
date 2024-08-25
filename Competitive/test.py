grid = [1,2,3,4,4,7]

low = 0
high = len(grid)-1
target = 4 
ans=0

while (low <= high):
    mid = low + (high-low)//2
    if(grid[mid] > target):
        ans=mid
        high = mid-1
    else:
        low =mid+1

print(low)