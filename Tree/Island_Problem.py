
import collections

visited=set()
q=collections.deque()
directions = [[1,0],[-1,0],[0,1],[0,-1]]
# not checking diagonally 

def bfs(i,j):
    q.append((i,j))
    visited.add((i,j))
    while q:
        r,c = q.popleft()
        for m,n in directions:
            row = r+m
            col = c+n
            if(row in range(rows) and col in range(cols)
               and grid[row][col]==1 and (row,col) not in visited):   # First condition is very important
                visited.add((row,col))
                q.append((row,col))

grid = [[1,1,1,0,1,0,1],
        [1,1,0,0,1,0,1],
        [1,0,0,1,1,0,0]]
rows=len(grid)
cols=len(grid[0])

count=0
for i in range(rows):
    for j in range(cols):
        if( grid[i][j]==1 and (i,j) not in visited):
            bfs(i,j)
            count+=1

print(count)
        