# https://www.geeksforgeeks.org/problems/cheapest-flights-within-k-stops/1
# https://youtu.be/9XybHVqTHcQ

"""
Input:
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
Output:
700
Explanation:
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
"""

from collections import deque

class Solution:

    def CheapestFLight(self, n, flights, src, dst, k):
        adj=[[] for _ in range(n)]
        for a,b,c in flights:
            adj[a].append([b,c])
        
        q= deque()
        dist=[float('inf')]*n
        dist[src]=0
        q.append((0,0,src))
        
        while q:
            kth, d, node = q.popleft()
            if kth > k:
                continue
            for subN,wt in adj[node]:
                if wt+d < dist[subN] and kth<=k:
                    dist[subN]=wt+d
                    q.append((kth+1, wt+d, subN))
        
        if dist[dst]==float('inf'):
            return -1
        return dist[dst]
                
obj=Solution()
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(obj.CheapestFLight(n,flights,src, dst, k))