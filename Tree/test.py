from collections import deque

q= deque()
visited = set()
directions = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1]]

def bfs(i,j):
    q.append((i,j))
    visited.add((i,j))
    while q:
        ro, co = q.popleft()
        for m,n in directions:
            nro, ncol = ro+m, co+n
            if(nro in range(row) and ncol in range(col) and 
               grid[nro][ncol]==1 and (nro,ncol) not in visited):
                visited.add((nro,ncol))
                q.append((nro,ncol))

grid = [[1,1,1,0,1,0,1],
        [1,1,0,0,1,0,1],
        [1,0,1,1,1,0,0]]

row = len(grid)
col = len(grid[0])
cnt =0 

for i in range(row):
    for j in range(col):
        if(grid[i][j]==1 and (i,j) not in visited):
            bfs(i,j)
            cnt += 1

print("The total island is: ", cnt)
