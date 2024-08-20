
def first_occur(arr):
    low=0
    high=len(arr)-1
    while (low <= high):
        mid = low + (high-low)//2
        if((mid ==0 or arr[mid-1]==0) and arr[mid]==1):
            return mid
        else:
            if(arr[mid]==0):
                low = mid + 1
            else:
                high= mid -1
    return -1


def max_1(mat):
    ans = 0
    anspos=0
    for i in range(len(mat)):
        val = first_occur(mat[i])
        if(val != -1):
            total = len(mat[i])-val
            if(ans<total):
                ans=total
                anspos=i
    return anspos

matrix = [[0, 1, 1, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 0],[1, 1, 1, 1]]

print(max_1(matrix))