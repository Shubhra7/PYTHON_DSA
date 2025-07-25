# https://leetcode.com/problems/number-of-provinces/



# Striver technique (** Using disjoint set union **)
class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.size=[1 for _ in range(n)]
    def findUp(self,u):
        if self.parent[u]==u:
            return u
        self.parent[u] = self.findUp(self.parent[u])
        return self.parent[u]
    def unionBySize(self,u,v):
        ulp_u=self.findUp(u)
        ulp_v=self.findUp(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] > self.size[ulp_v]:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
        else:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]

        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        ds= DisjointSet(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    ds.unionBySize(i,j)
        cnt=0
        for i in range(n):
            if ds.parent[i]==i:
                cnt+=1
        return cnt

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
