# https://youtu.be/iTBaI90lpDQ?si=znme9S61C5NPBOVf
# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

from collections import deque
class Solution:
    def isCycle(self, V, edges):
        # code here
        ##############################
        # Using Topological sort(BFS)
        ##############################
        adj=[[] for _ in range(V)]
        indeg=[0]*V
        for u,v in edges:
            adj[u].append(v)
        for i in range(V):
            for subN in adj[i]:
                indeg[subN]+=1
        q=deque()
        for i in range(V):
            if indeg[i]==0:
                q.append(i)
        cnt=0
        while q:
            ele=q.popleft()
            cnt+=1
            for subN in adj[ele]:
                indeg[subN]-=1
                if indeg[subN]==0:
                    q.append(subN)
        if cnt!=V:
            return True
        return False
    
V = 4
edges =[[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]   #True
# edges= [[0, 1], [0, 2], [1, 2], [2, 3]]  #False
obj=Solution()
print("Cycle detection check: ",end=" ")
print(obj.isCycle(V,edges))   