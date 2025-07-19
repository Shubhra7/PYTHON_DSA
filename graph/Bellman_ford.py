# https://youtu.be/0vVofAhAYjc?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn
# https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1

"""
Input: V = 5
edges[][] = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]], src = 0

Output: [0, 5, 6, 6, 7]
Explanation: Shortest Paths:
For 0 to 1 minimum distance will be 5. By following path 0 → 1
For 0 to 2 minimum distance will be 6. By following path 0 → 1  → 2
For 0 to 3 minimum distance will be 6. By following path 0 → 1  → 2 → 4 → 3 
For 0 to 4 minimum distance will be 7. By following path 0 → 1  → 2 → 4
"""

class Solution:
    def bellmanFord(self, V, edges, src):
        # Initialize distance to all vertices as infinite, except source
        dist = [1e8] * V
        dist[src] = 0

        # Relax all edges V-1 times
        for i in range(V - 1):
            for u, v, wt in edges:
                if dist[u] < 1e8 and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt

        # Check for negative-weight cycles
        for u, v, wt in edges:
            if dist[u] < 1e8 and dist[u] + wt < dist[v]:
                return [-1]

        return dist

V = 5
edges= [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
src = 0

obj=Solution()
print(obj.bellmanFord(V,edges,src))
