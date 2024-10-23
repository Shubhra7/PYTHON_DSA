# link: https://www.naukri.com/code360/problems/frog-jump_3621012?leftPanelTabValue=PROBLEM
# video: Striver dp series (3rd video)

import sys
# arr=[7,4,4,2,6,6,3,4]
arr=[10,50,10]
dp=[0 for i in range(len(arr))]
dp[1]=abs(arr[1]-arr[0])
for i in range(1,len(arr)):
    leftval = dp[i-1] + abs(dp[i]-dp[i-1])
    rightval = sys.maxsize
    if(i>1):
        rightval = dp[i-2] + abs(dp[i]-dp[i-2])
    dp[i] = min(leftval,rightval)

print(dp)
print(dp[-1])
