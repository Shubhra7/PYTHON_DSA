from collections import deque

q= deque()
visited = set()
directions = [[1,0],[0,1],[-1,0],[0]]

def bfs(i,j):
    q.append((i,j))
    visited.add((i,j))
    while q:
        ro, co = q.popleft()

grid = [[1,1,1,0,1,0,1],
        [1,1,0,0,1,0,1],
        [1,0,0,1,1,0,0]]

row = len(grid)
col = len(grid[0])
cnt =0 

for i in range(row):
    for j in range(col):
        if(grid[i][j]==1):
            bfs(i,j)
            cnt += 1

print("The total island is: ", cnt)
