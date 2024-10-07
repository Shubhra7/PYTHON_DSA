def dfs(i,visited,ans):
    visited.add(i)
    ans.append(i)
    for j in adj[i]:
        if(j not in visited):
            dfs(j,visited,ans)

adj = [[1,2],[3,4],[5],[6],[],[],[]]

visited=set()
ans=[]
dfs(0,visited,ans)
print(ans)