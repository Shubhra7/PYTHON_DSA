import collections

q=collections.deque()



def bfs(i,j):
    q.append((i,j))
    visited.add((i,j))
    while q:
        r,c = q.popleft()
        for m,n in directions:
            row= r+m
            col=c+n
            if (row in range(rows) and col in range(cols)
                and grid[row][col]==1 and (row,col) not in visited):
                q.append((row,col))
                visited.add((row,col))
        # print(q)
        # print(visited)


visited=set()
directions=[[1,0],[-1,0],[0,1],[0,-1]]
grid=[[1,1,1,0,1],
      [1,1,0,0,1],
      [1,0,0,0,0]]

rows=len(grid)
cols=len(grid[0])

ans=0
for i in range(rows):
    for j in range(cols):
        if(grid[i][j]==1 and (i,j) not in visited):
            bfs(i,j)
            ans+=1

print("Total island: ",ans)
print("BFS is: ",visited)