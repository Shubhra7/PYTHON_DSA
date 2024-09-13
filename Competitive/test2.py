import bisect

def countSm(m,row,mid):
    count = 0
    for i in range(row):
        count += bisect.bisect_right(m[i],mid)
    return count

def median(m,row,col):
    low = min([m[i][0] for i in range(row)])
    high = max([m[i][col-1] for i in range(row)])
    req = (row*col)//2
    while(low <= high):
        mid = low + (high-low)//2
        smallEq = countSm(m,row,mid)
        if(smallEq > req):
            high = mid -1
        else:
            low = mid + 1
    return low


matrix = [ [ 1, 5, 7, 9, 11 ],
            [ 2, 3, 4, 8, 9 ],
            [ 4, 11, 14, 19, 20 ],
            [ 6,13, 22, 99, 100 ],
            [ 7, 15, 17, 24, 28 ]   ]


print(median(matrix,len(matrix),len(matrix[0])))
