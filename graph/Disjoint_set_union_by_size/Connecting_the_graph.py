# https://youtu.be/FYrl7iz9_ZU?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn
# https://www.geeksforgeeks.org/problems/connecting-the-graph/1

"""
Input:
n = 4
m = 3
Edges = [ [0, 1] , [0, 2] , [1, 2] ]
Output:
1
Explanation:
Remove edge between vertices 1 and 2 and add between vertices 1 and 3.
"""

# for connecting n component we need minimum n-1 edges
# so first count the extra edges
# then count the prime parent so it will create seperate components
# then to connect n prime parent we need n-1 edges
# so then check extras and ans so if possible or not to connect

class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]
        
    def findUp(self,u):
        if self.parent[u]==u:
            return u
        self.parent[u] = self.findUp(self.parent[u])
        return self.parent[u]
        
    def unionBySize(self,u,v):
        ulp_u = self.findUp(u)
        ulp_v = self.findUp(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] > self.size[ulp_v]:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
        else:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
            
class Solution:
    def Solve(self, n, adj):
        # Code here
        ds=DisjointSet(n)
        extras=0
        for u,v in adj:
            if ds.findUp(u) == ds.findUp(v):
                extras +=1
            else:
                ds.unionBySize(u,v)
        
        ans = 0
        for i in range(n):
            if ds.parent[i] == i:
                ans += 1
        ans = ans-1  #for connecting n nodes we need min n-1 edges
        if ans <= extras:
            return ans
        return -1
                
        
obj = Solution()
n = 4
Edges = [ [0, 1] , [0, 2] , [1, 2] ]
print(obj.Solve(n,Edges))
