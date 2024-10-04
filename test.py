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

for i in range(0,len(pairs)):
    a= pairs[i][0]
    b= pairs[i][1]
    prefB = premap[a][b]
    prefA = premap[b][a]
    for j in range(i+1,len(pairs)):
        ele1 = pairs[j][0]
        ele2 = pairs[j][1]
        prefEle2 = premap[ele1][ele2]
        prefEle1 = premap[ele2][ele1]

        if(prefB > premap[a][ele1] and prefEle2 > premap[ele1][a]):
            flag[a]= True
            flag[ele1]= True

        if(prefB > premap[a][ele2] and prefEle1 > premap[ele2][a]):
            flag[a]=True
            flag[ele2] = True
        
        

