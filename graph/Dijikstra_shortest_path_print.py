# https://www.youtube.com/watch?v=rp1SMw7HSO8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=35
# https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1

"""
Input: n = 5, m= 6, edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
Output: 5
Explanation: Shortest path from 1 to n is by the path 1 4 3 5 whose weight is 5. 
"""

# DO like dijikstra almost
# addition use Parent array for store
# then last backtrack for getting the shortest path

from typing import List
import heapq
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        adj=[[] for _ in range(n)]
        for u,v,wt in edges:
            adj[u-1].append([v-1,wt])
            adj[v-1].append([u-1,wt])
        dist=[1e8]*n
        parent=[i for i in range(0,n)]
        
        q=[]
        heapq.heappush(q,(0,0))
        dist[0]=0
        while q:
            dis,node = heapq.heappop(q)
            for subNode,edgW in adj[node]:
                if edgW+dis < dist[subNode]:
                    dist[subNode] = edgW+dis
                    parent[subNode]=node
                    heapq.heappush(q,(dist[subNode],subNode))
        
        if dist[n-1]==1e8:
            return [-1]
        
        ans=[]
        node=n-1
        while parent[node]!=node:
            ans.append(node+1)
            node=parent[node]
        ans.append(1)
        # ans.append(dist[-1]) #follow question want
        return ans[::-1]

obj=Solution()
n = 5 
m= 6 
edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]     
print(obj.shortestPath(n,m,edges)) 
            
        
