N = 5

def print_mat(mat):
    for i in range(len(mat)):
        print(mat[i])


def findMaxValue(mat):
    maxValue = -100

    maxArr = [[0] * N for z in range(N)]

    maxArr[N - 1][N - 1] = mat[N - 1][N - 1]
    maxv = mat[N - 1][N - 1]

    # print(maxv)

    for j in range(N - 2, -1, -1):
        if mat[N - 1][j] > maxv:
            maxv = mat[N - 1][j]
        maxArr[N - 1][j] = maxv
    
    print_mat(maxArr)
    

    maxv = mat[N - 1][N - 1]

    for i in range(N - 2, -1, -1):
        if mat[i][N - 1] > maxv:
            maxv = mat[i][N - 1]
        maxArr[i][N - 1] = maxv
    print()
    print_mat(maxArr)
    print()

    for i in range(N - 2, -1, -1):
        for j in range(N - 2, -1, -1):
            if maxArr[i + 1][j + 1] - mat[i][j] > maxValue:
                maxValue = maxArr[i + 1][j + 1] - mat[i][j]
            maxArr[i][j] = max(mat[i][j], max(maxArr[i][j + 1], maxArr[i + 1][j]))
            print_mat(maxArr)
            print()

    return maxValue


matrix = [[ 1,  2, -1, -4, -20],
          [-8, -3,  4,  2,   1],
          [ 3,  8,  6,  1,   3],
          [-4, -1,  1,  7,  -6],
          [ 0, -4, 10, -5,   1]]

print("Maximum Value is", findMaxValue(matrix))