# https://youtu.be/WeoxPsb_p0U
# https://www.geeksforgeeks.org/problems/activity-selection-1587115620/1
"""
Input: start[] = [1, 3, 0, 5, 8, 5], 
finish[] = [2, 4, 6, 7, 9, 9]
Output: 4
"""

class Solution:
    def activitySelection(self, start, finish):
        #code here
        i=0
        n=len(start)
        temp=[]
        while i<n:
            temp.append([start[i],finish[i]])
            i+=1
        temp.sort(key=lambda x:x[1]) #important line
        count=1
        curfin=temp[0][1]
        for i in range(1,n):
            if temp[i][0]>curfin:
                count+=1
                curfin=temp[i][1]
        return count

obj=Solution()
print(obj.activitySelection([1, 3, 0, 5, 8, 5],[2, 4, 6, 7, 9, 9]))  #o/p=4