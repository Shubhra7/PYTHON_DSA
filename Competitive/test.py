import bisect

def total_1(arr,val):
    ans = bisect.bisect_left(arr,val)
    return (len(arr)-ans)


def max_1_row(matrix):
    maxi=-1
    maxpos=-1
    for i in range(len(matrix)):
        val = total_1(matrix[i],1)
        if(val > maxi):
            maxi = val
            maxpos = i
    return maxpos



matrix = [[1, 1, 1, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 0],[1, 1, 1, 1]]

print(max_1_row(matrix))