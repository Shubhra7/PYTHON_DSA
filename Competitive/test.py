grid = [[1,2,3],
        [4,3,1]]

r = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
print(r)

for i in range(len(r)):
    r[i]=r[i][::-1]

print(r)