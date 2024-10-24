# Frog can jump k distance max

import sys

arr = [7,4,4,2,6,6,3,4]
dp = [0 for i in range(len(arr))]
k=4

for i in range(1,len(dp)):
    min_step = sys.maxsize
    for j in range(1,k+1):
        if(i-j >= 0):
            jump = dp[i-j] + abs(arr[i]-arr[i-j])
            min_step = min(min_step,jump)
        else:
            break
    dp[i]=min_step

print(dp[-1])
            