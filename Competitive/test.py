import collections 

grid = [[1,0,1,1,1],
        [1,0,0,1,1],
        [0,0,0,0,1]]

visited=set()
q= collections.deque()
directions = [[1,0],[-1,0],[0,1],[0,-1]]

row = len(grid)
col = len(grid[0])
count=0
for i in range(row):
    for j in range(col):
        if (grid[i][j] == 1):
            bfs(i,j)
            count+=1