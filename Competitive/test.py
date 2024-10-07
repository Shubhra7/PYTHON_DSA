from collections import deque

def bfs(start,visited,ans,adj):
    q = deque()
    q.append(start)
    ans.append(start)
    visited.add(start)
    while q:
        item = q.popleft()
        for i in adj[item]:
            if(i not in visited):
                q.append(i)
                visited.add(i)
                ans.append(i)
        

adj = [[1,2],[3,4],[5],[6],[],[],[]]

ans =[]
visited = set()
bfs(0,visited,ans,adj)
print(ans)

