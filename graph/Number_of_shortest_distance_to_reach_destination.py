# https://youtu.be/_-0mx0SmYxA?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn
# https://www.geeksforgeeks.org/problems/number-of-ways-to-arrive-at-destination/1

"""
Example 1:

Input:
n=7, m=10
edges= [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

Output:
4
Explaination:

The four ways to get there in 7 minutes are:
- 0  6
- 0  4  6
- 0  1  2  5  6
- 0  1  3  5  6
"""

from typing import List
from collections import defaultdict
import sys
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #Your code here
        adj=[[] for _ in range(n)]
        for u,v,wt in roads:
            adj[u].append([v,wt])
            adj[v].append([u,wt])
        dist=[float('inf')]*n
        ways=[0]*n
        mod=int((1e9)+7)
        
        q=[]
        ways[0]=1
        dist[0]=0
        heapq.heappush(q,[0,0])
        while q:
            wt,node = heapq.heappop(q)
            for subN,edgeW in adj[node]:
                if wt+edgeW < dist[subN]:
                    dist[subN]=wt+edgeW
                    ways[subN] = ways[node]
                    heapq.heappush(q,[wt+edgeW, subN])
                elif wt+edgeW == dist[subN]:
                    ways[subN] = (ways[subN] + ways[node]) % mod
        return ways[-1]%mod
                    
obj=Solution()
n=7 
edges= [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

print(obj.countPaths(n,edges))