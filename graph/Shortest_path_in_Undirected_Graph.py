"""
Input: adj[][] = [[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]], src=0
Output: [0, 1, 2, 1, 2, 3, 3, 4, 4]
"""

"""
                            **************** WHY NOT DFS ***********
BFS is optimal for finding shortest paths in an unweighted graph because it explores nodes level by level, guaranteeing that the first time you reach a node is via the shortest possible path.

DFS does not explore in order of increasing distance. It can go deep down one path without considering shorter alternative paths first — so if you use DFS, you’d have to track and compare path lengths manually, and there’s no guarantee it would be efficient or correct without backtracking and revisiting nodes.
"""

from collections import deque
class Solution:
    def shortestPath(self, adj, src):
        # code here
        ###############################
        # Used BFS because the BFS stored the node 
        # in queue according to the ascending distances
        # so easy to track
        ##################################
        q=deque()
        dist=[1e8]*len(adj)
        dist[src]=0
        q.append(src)
        while q:
            ele=q.popleft()
            for it in adj[ele]:
                if dist[it] > dist[ele]+1:
                    dist[it]= dist[ele]+1
                    q.append(it)
        for i in range(len(dist)):
            if dist[i]==1e8:
                dist[i]=-1
        return dist

adj=[[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]]
src=0
obj=Solution()
print("Shortest distances in Directed Graph: ",end=" ")
print(obj.shortestPath(adj,src))
