grid = [[1,2,3],
        [8,9,4],
        [7,6,5]]

row = len(grid)
col = len(grid[0])

up = 0
down = row - 1
left = 0
right = col - 1

while ( up <= down and left <= right):
    for i in range(left,right + 1):
        print(grid[up][i],end=" ")
    up += 1
    
    for i in range(up,down+1):
        print(grid[i][right],end=" ")
    right -= 1

    for i in range(right,left-1,-1):
        print(grid[down][i],end=" ")
    down -= 1
    # print("Hl",down," ",up," hi",end="  ")

    for j in range(down,up-1,-1):
        # print("heelo","(",left,j,")",end="  ")
        print(grid[j][left],end=" ")
    left += 1