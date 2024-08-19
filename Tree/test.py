import bisect
def lowerbound(matrix,index):
    count = 0
    for i in range(len(matrix)):
        count += bisect.bisect_left(matrix[i],index)
    return count+1

def median(matrix,row,col):
    low = min([matrix[i][0] for i in range(len(matrix))])
    high = max([matrix[i][col-1] for i in range(len(matrix))])
    req = (row*col)//2
    while (low <= high):
        mid = low + (high - low)//2
        smallEqual = lowerbound(matrix,mid)
        if (req >= smallEqual):
            low = mid + 1
        else:
            high = mid - 1
    return low

matrix = [     [ 1, 5, 7, 9, 11 ],
      [ 2, 3, 4, 8, 9 ],
      [ 4, 11, 14, 19, 20 ],
      [ 6, 10, 22, 99, 100 ],
      [ 7, 15, 17, 24, 28 ]   ]

print(median(matrix,len(matrix),len(matrix[0])))