def dfs(i,visited,ans):
    visited.add(i)
    for j in adj[i]:
        if(j not in visited):
            ans.append(j)
            dfs(j,visited,ans)

adj = [[1,2],[3,4],[5],[6],[],[],[]]

visited=set()
ans=[]
for i in range(7):
    dfs(i,visited,ans)
print(ans)