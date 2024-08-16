
## **** applicable only when each row is sorted..
# Link: https://prepinsta.com/cpp-program/find-row-with-maximum-number-of-1s/

def first_1(mat):
    left =0
    right = len(mat)-1
    while left <= right:
        mid = left + (right-left)//2
        if ((mid==0 or mat[mid-1]==0) and mat[mid]==1):
            return mid
        elif (mat[mid]==0):
            left = mid + 1
        else:
            right = mid - 1
    return -1

def max_1(mat):
    ans = 0
    anspos=0
    for i in range(len(mat)):
        val = first_1(mat[i])
        # print(val)
        if (val != -1):
            total1 = len(mat[i]) - val
        # print(total1)
        # print()
        if (ans < total1):
            ans = total1
            anspos = i
    return anspos
            

matrix = [[0, 1, 1, 1],
          [1, 1, 1, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 0]]

print(max_1(matrix))