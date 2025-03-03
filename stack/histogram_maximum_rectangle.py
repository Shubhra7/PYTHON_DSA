# https://www.naukri.com/code360/problems/largest-rectangle-in-a-histogram_1058184?leftPanelTabValue=PROBLEM
# https://youtu.be/Bzat9vgD0fs?si=ZuCjJGtqROiOaLZH

"""
Input: arr[] = [60, 20, 50, 40, 10, 50, 60]
Output: 100
Explanation: We get the maximum by picking bars highlighted above in green (50, and 60).
The area is computed (smallest height) * (no. of the picked bars) = 50 * 2 = 100.
"""

def largestRectangle(arr):
    # Write your code here.
    maxi=0
    stack=[]
    for i in range(len(arr)):
        while stack and arr[stack[-1]]>arr[i]:
            height=arr[stack.pop()]
            nse=i
            pse=stack[-1] if stack else -1 
            maxi=max(maxi,height*(nse-pse-1))  #area formula with pse and nse
        stack.append(i)
    while stack:
        height=arr[stack.pop()]
        nse=len(arr)  #For lastest 
        pse=stack[-1] if stack else -1 
        maxi=max(maxi,height*(nse-pse-1))
    return maxi

print(largestRectangle([60, 20, 50, 40, 10, 50, 60]))  #o/p=>100