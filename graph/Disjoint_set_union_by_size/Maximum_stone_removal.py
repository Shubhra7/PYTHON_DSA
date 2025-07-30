# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
# https://youtu.be/OwMNX8SPavM?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn

"""
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
"""

# Formula =  Total_node - number_of_components

from typing import List

class DisjoinSet:
    def __init__(self,n):
        self.size=[1 for _ in range(n)]
        self.parent=[i for i in range(n)]
    def findUp(self,u):
        if self.parent[u]==u:
            return u
        self.parent[u] = self.findUp(self.parent[u])
        return self.parent[u]
    def unionBySize(self,u,v):
        ulp_u=self.findUp(u)
        ulp_v=self.findUp(v)
        if ulp_u==ulp_v:
            return
        if self.size[ulp_u] > self.size[ulp_v]:
            self.parent[ulp_v]=ulp_u
            self.size[ulp_u] += self.size[ulp_v]
        else:
            self.parent[ulp_u]=ulp_v
            self.size[ulp_v] += self.size[ulp_u]

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        maxRow,maxCol=0,0
        for row,col in stones:
            maxRow=max(maxRow,row)
            maxCol=max(maxCol,col)
        ds = DisjoinSet(maxRow + maxCol + 2)
        stonesNode = set()
        for it in stones:
            nodeRow = it[0]
            nodeCol = it[1] + maxRow + 1   #Forumla to convert the column into node number
            ds.unionBySize(nodeRow,nodeCol)
            stonesNode.add(nodeRow)
            stonesNode.add(nodeCol)
        
        cnt=0
        for it in stonesNode:
            if ds.findUp(it) == it:
                cnt+=1
        return n-cnt

stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
obj=Solution()
print(obj.removeStones(stones))
        