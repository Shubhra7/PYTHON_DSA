
import collections

q=collections.deque()
directions=[[1,0],[-1,0],[0,1],[0,-1]]
visited=[]


def bfs(i,j):
    visited.append((i,j))
    q.append((i,j))
    while q:
        m,n = q.popleft()
        for r,c in directions:
            row = m + r
            col = n + c
            if(row in range(rows) and col in range(cols)
            and grid[row][col]==1 and (row,col) not in visited):
                q.append((row,col))
                visited.append((row,col))
        




grid=[[1,1,1,0,1],
      [1,1,0,0,1],
      [1,1,0,1,1]]

rows=len(grid)
cols=len(grid[0])

count=0

for i in range(rows):
    for j in range(cols):
        if(grid[i][j]==1 and (i,j) not in visited):
            bfs(i,j)
            count+=1

print(count)
print("The BFS search is: ",visited)
        