# https://youtu.be/mJcZjjKzeqk?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn
# https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1


from typing import List
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        q=[]
        visit=[0]*V
        heapq.heappush(q,[0,0])
        summ=0
        while q:
            wt,node = heapq.heappop(q)
            if visit[node]==1:
                continue
            visit[node]=1
            summ+=wt
            for adjNode,edW in adj[node]:
                if visit[adjNode]!=1:
                    heapq.heappush(q,[edW,adjNode])
        return summ
                
        
V = 3
E = 3
adj = [[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]]]
obj=Solution()
print(obj.spanningTree(V,adj))