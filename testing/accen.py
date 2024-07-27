import collections
def bfs(i,j):
    q.append((i,j))
    visited.add((i,j))
    while q:
        r,c =q.popleft()
        for m,n in direction:
            rows = r+m
            cols= c+n
            if (rows in range(row) and cols in range(col)
                and grid[rows][cols]==1 and (rows,cols) not in visited):
                q.append((rows,cols))
                visited.add((rows,cols))



grid =[[1,1,0,1],
       [1,1,0,1],
       [1,0,0,0]]

q=collections.deque()
direction=[[1,0],[-1,0],[0,1],[0,-1]]

visited=set()

row=len(grid)
col=len(grid[0])
count=0

for i in range(row):
    for j in range(col):
        if(grid[i][j]==1 and (i,j) not in visited):
            bfs(i,j)
            count+=1

print(count)