grid = [[1,2,3],
        [5,5,5]]

res = [[grid[j][i] for j in range(len(grid))]for i in range(len(grid[0]))]

for i in res:
    print(i)