# https://youtu.be/IexN60k62jo?si=Ef_gn2vW2mMDtrbx
# https://leetcode.com/problems/merge-intervals/description/

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
 and return an array of the non-overlapping intervals that cover all the intervals in the input.
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
def mergeIntervals(intervals):
    # Write your code here
    n=len(intervals)
    intervals.sort()
    ans=[]
    for i in range(n):
        if( len(ans)==0 or intervals[i][0]>ans[-1][1]):
            ans.append(intervals[i])
        else:
            ans[-1][1]=max(ans[-1][1],intervals[i][1])
    return ans

print(mergeIntervals())
