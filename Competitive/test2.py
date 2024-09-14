# grid=["*.*#***",
#       "*.*#*.*",
#       "***#***"]
# n=7
# -------------------------------
# grid=["*.*#***#***.*.",
#       "*.*#*.*#******",
#       "***#***#****.*"]

# n=14
# ----------------------------------------
# grid=["*.*#***#***#***.*.",
#       "*.*#*.*#.*.#******",
#       "***#***#***#****.*"]

# n=18
# --------------------------------------------

grid=["*.*#.***#.*.",
      "*.*#..*.#***",
      "***#.***#*.*"]
n=12

l=[]

for k in range(3):   # For each string
    i=0
    singleGrid=grid[k]   # store the string into a variable
    print(singleGrid)
    maa=[]
    while i<n:
        p=[]
        for j in range(3):
            if(singleGrid[i+j]=='*'):
                p.append('*')
            if(singleGrid[i+j]=='.'):
                p.append('.')
        if(i+j+1) in range(n-1) and (singleGrid[i+j+1]=='#'):
            p.append('#')
            i += 4
        else:
            i+=3
        # print(i," : ",n)
        print(p)
        maa.append(p)
    l.append(maa)
    print()

for i in l:
    print(i)
print(len(l[0]))
po=len(l[0])

print(l[0][1])

ans=""
m=0
for i in range(po):
    if l[m][i]==['*', '.', '*', '#'] or l[m][i]==['*', '.', '*']:
        if l[m+1][i] == ['*', '.', '*', '#'] or l[m+1][i] == ['*', '.', '*']:
            if l[m+2][i] == ['*', '*', '*', '#'] or l[m+2][i] == ['*', '*', '*']:
                # print("U")
                ans += "U"
                val = l[m+2][i]
                if(val[-1]=='#'):
                    ans = ans + "#"

    if l[m][i]==['*', '*', '*', '#'] or l[m][i]==['*', '*', '*']:
        if l[m+1][i] == ['*', '.', '*', '#'] or l[m+1][i] == ['*', '.', '*']:
            if l[m+2][i] == ['*', '*', '*', '#'] or l[m+2][i] == ['*', '*', '*']:
                # print("O")
                ans += "O"
                val = l[m+2][i]
                if(val[-1]=='#'):
                    ans = ans + "#"

    if l[m][i]==['*', '*', '*'] or l[m][i]==['*', '*', '*','#']:
        if l[m+1][i] == ['.', '*', '.'] or l[m+1][i] == ['.', '*', '.','#']:
            if l[m+2][i] == ['*', '*', '*'] or l[m+2][i] == ['*', '*', '*','#']:
                # print("I")
                ans += "I"
                val = l[m+2][i]
                if(val[-1]=='#'):
                    ans = ans + "#"

    if l[m][i]==['*', '*', '*'] or l[m][i]==['*', '*', '*','#']:
        if l[m+1][i] == ['*', '*', '*'] or l[m+1][i] == ['*', '*', '*','#']:
            if l[m+2][i] == ['*', '*', '*'] or l[m+2][i] == ['*', '*', '*','#']:
                # print("E")
                ans += "E"
                val = l[m+2][i]
                if(val[-1]=='#'):
                    ans = ans + "#"

    if l[m][i]==['.', '*', '.'] or l[m][i]==['.', '*', '.','#']:
        if l[m+1][i] == ['*', '*', '*'] or l[m+1][i] == ['*', '*', '*','#']:
            if l[m+2][i] == ['*', '.', '*'] or l[m+2][i] == ['*', '.', '*','#']:
                # print("A")
                ans += "A"
                val = l[m+2][i]
                if(val[-1]=='#'):
                    ans = ans + "#"
    
    if l[m][i]==['.', '*', '*'] or l[m][i]==['.', '*', '*','#']:
        if l[m+1][i] == ['*', '*', '*'] or l[m+1][i] == ['*', '*', '*','#']:
            if l[m+2][i] == ['*', '*', '*'] or l[m+2][i] == ['*', '*', '*','#']:
                # print("E")
                ans += "E"
                val = l[m+2][i]
                if(val[-1]=='#'):
                    ans = ans + "#"

# ans = ans[::-1]
print(ans)


    


    