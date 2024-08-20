grid = [[0,1,2,3],
        [4,5,6,7],
        [8,9,10,11]]

row = len(grid)
col = len(grid[0])

high = row*col
low = 0
search = 11
flag=0

while (low<=high):
    mid = low + (high-low)//2
    val= grid[mid // col][mid % col] 
    if(val == search):
        flag=1
        print("place: ",(mid//col)," ",(mid%col))
        break
    elif(val < search):
            low = mid + 1
    else:
         high = mid - 1

if(flag == 0):
     print("Not found")