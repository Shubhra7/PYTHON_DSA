# https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
# https://youtu.be/AsGzwR_FWok
"""
Input: arr[] = [900, 940, 950, 1100, 1500, 1800],
dep[] = [910, 1200, 1120, 1130, 1900, 2000]
Output: 3

Explanation: There are three trains during the time 9:40 to 12:00. 
So we need a minimum of 3 platforms.
"""

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        n=len(arr)
        i=0
        j=0
        count=0
        maxi=0
        while i<n:
            if arr[i]<=dep[j]: #Important line
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            maxi=max(maxi,count)
        return maxi

obj=Solution()
print(obj.minimumPlatform([900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000]))
#o/p==3
