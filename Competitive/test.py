grid=[[1,2,3,4],
      [2,1,3,6],
      [3,0,0,1],
      [0,0,0,0]]

sum = 0
n=len(grid[0])
re=[]
for i in range(len(grid)):
        for j in range(len(grid[0])):
                if (i==j or (i+j+1)==n):
                        re.append(grid[i][j])
                        sum = sum + grid[i][j]

print(sum)
print(re)
