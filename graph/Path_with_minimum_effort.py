# https://youtu.be/0ytpZyiZFhA?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn


"""
Input:
row = 3
columns = 3 
heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 
2
"""
from typing import List
import heapq

class Solution:
    def MinimumEffort(self, rows : int, columns : int, heights : List[List[int]]) -> int:
        # code here
        q=[]
        dist=[[float('inf')]*columns for _ in range(rows)]
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        heapq.heappush(q,(0,[0,0]))
        
        while q:
            diff, ele=heapq.heappop(q)
            r,c=ele[0],ele[1]
            
            if r==rows-1 and c==columns-1:
                return diff
            for u,v in directions:
                newR,newC = r+u,c+v
                if newR in range(rows) and newC in range(columns):
                    newEff = max(diff,abs(heights[r][c]-heights[newR][newC]))
                    if newEff < dist[newR][newC]:
                        dist[newR][newC]=newEff
                        heapq.heappush(q,(newEff,[newR,newC]))
        return 0
        
        
obj=Solution()
row = 3
columns = 3 
heights = [[1,2,2],[3,8,2],[5,3,5]]
print("The minimum path cost would be: ",end=" ")
print(obj.MinimumEffort(row,columns, heights))