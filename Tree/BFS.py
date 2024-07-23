
import collections


q=collections.deque()
directions=[[1,0],[-1,0],[0,1],[0,-1]]
visited=set()


def bfs(i,j):
    for r,c in directions:
        row= i + r
        col = j + c
        if(row)




grid=[[1,1,1,0,1],
      [1,1,0,0,1],
      [1,1,0,1,1]]

rows=len(grid)
cols=len(grid[0])

for i in range(rows):
    for j in range(cols):
        bfs(i,j)