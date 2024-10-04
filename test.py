n=4
preferences = [[1,2,3], [3,2,0], [3,1,0], [1,2,0]]  
pairs = [[0,1], [2,3]]

premap = [[99 for i in range(n)] for i in range(n)]

for i in range(0,n):
    for j in range(0,n-1):
        premap[i][preferences[i][j]] = j

for i in premap:
    print(i)

flag = [False for i in range(n)]


