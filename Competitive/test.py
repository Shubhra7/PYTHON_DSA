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

# n=18   U#O#I#EA
# --------------------------------------------

# grid=["*.*#.***#.*.",
#       "*.*#..*.#***",
#       "***#.***#*.*"]
# n=12

n=int(input())
co=[]
for i in range(3):
    co.append(list(input().split()))

print("The ceo is: ")
for i in co:
    print(i)

print()
i=0
while i<n-2:    
    if co[0][i]=='#':       
         print("#",end="")        
         i+=1        
         continue   
    if co[0][i]=='.' and co[0][i+1]=='*' and co[0][i+2]=='.':
          if co[1][i]=='*' and co[1][i+1]=='*' and co[1][i+2]=='*':            
              if co[2][i]=='*' and co[2][i+1]=='.' and co[2][i+2]=='*':                
                  print('A',end="")    
    if co[0][i]=='*' and co[0][i+1]=='*' and co[0][i+2]=='*':        
        if co[1][i]=='*' and co[1][i+1]=='*' and co[1][i+2]=='*':            
            if co[2][i]=='*' and co[2][i+1]=='*' and co[2][i+2]=='*':                
                print('E',end="")                
                i+=3                
                continue        
        elif co[1][i]=='.' and co[1][i+1]=='*' and co[1][i+2]=='.':            
                if co[2][i]=='*' and co[2][i+1]=='*' and co[2][i+2]=='*':                
                    print('I',end="")                
                    i+=3                
                    continue        
        elif co[1][i]=='*' and co[1][i+1]=='.' and co[1][i+2]=='*':            
            if co[2][i]=='*' and co[2][i+1]=='*' and co[2][i+2]=='*':                
                print('O',end="")                
                i+=3               
                continue    
    if co[0][i]=='*' and co[0][i+1]=='.' and co[0][i+2]=='*':        
        if co[1][i]=='*' and co[1][i+1]=='.' and co[1][i+2]=='*':            
            if co[2][i]=='*' and co[2][i+1]=='*' and co[2][i+2]=='*':                
                print('U',end="")                
                i+=3                
                continue    
    i+=1