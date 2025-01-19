"""
Given n non-negative integers representing an elevation 
map where the width of each bar is 1, compute how much water it can trap after raining.
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
 In this case, 6 units of rain water (blue section) are being trapped.
"""

def trap(height):
        total,l = 0,0
        r=len(height)-1
        leftMaxi=0
        rightMaxi=0
        while l<r:
            if height[l]<=height[r]:
                if leftMaxi > height[l]:
                    total += leftMaxi - height[l]
                else:
                    leftMaxi=height[l]
                l+=1
            else:
                if rightMaxi > height[r]:
                    total += rightMaxi - height[r]
                else:
                    rightMaxi = height[r]
                r-=1
        return total

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))   #O/P ==> 6