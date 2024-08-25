import collections

grid = [[2,1,1],
        [1,1,2],
        [0,1,1]]


visited=set()
directions = [[1,0],[-1,0],[0,1],[0,-1]]
q = collections.deque()
row =len(grid)
col =len(grid(0))
fresh=set()

for i in range(row):
    for j in range(col):
        
