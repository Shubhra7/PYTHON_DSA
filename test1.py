import collections
visited=set()
d=collections.deque()
direction = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]


def bfs(i,j):
    d.append((i,j))
    visited.add((i,j))
    while d:
        r,c = d.popleft()
        for m,n in direction:
            ro,co = m+r,n+c
            if(ro in range(row) and co in range(col) and
                grid[ro][co]==1 and (ro,co) not in visited):
                d.append((ro,co))
                visited.add((ro,co))


grid = [[1,1,0,0,1],
        [1,1,0,0,1],
        [1,0,1,0,0]]

# Island problem

row = len(grid)
col = len(grid[0])
count = 0

for i in range(row):
    for j in range(col):
        if(grid[i][j]==1 and (i,j) not in visited):
            bfs(i,j)
            count += 1
print("The number of island is: ",count)