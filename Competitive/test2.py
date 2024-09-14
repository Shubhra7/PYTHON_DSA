grid=["*.*#***",
      "*.*#*.*",
      "***#***"]

n=7
l=[]

for k in range(3):   # For each string
    i=0
    singleGrid=grid[k]   # store the stirng into a variable
    print(singleGrid)
    while i<n:
        p=[]
        for j in range(2):
            if(singleGrid[i+j]=='*'):
                p.append('*')
            if(singleGrid[i+j]=='.'):
                p.append('.')
        if(i+j+1) in range(n-1) and (singleGrid[i+j+1]=='#'):
            p.append('#')
            i += 3
        i+=2
        print(p)


    