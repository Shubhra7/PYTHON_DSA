# https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1from collections import deque

from collections import deque
def bfs(node,adj,visit,ans):
    visit[node]=1
    q=deque()
    q.append(node)
    while q:
        nd=q.popleft()
        ans.append(nd)
        for i in adj[nd]:
            if visit[i]==0:
                visit[i]=1
                q.append(i)



adj=[[2,3,1],[0],[0,4],[0],[2]]
ans=[]
V=len(adj)
visit=[0]*V
bfs(0,adj,visit,ans)
print("The BFS traversal answer is: ",ans)