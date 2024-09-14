# # Link: https://prepinstaprime.com/course/tcs-codevita
# Problem Description
# Three characters { #, *, . } represents a constellation of stars and galaxies in space. Each galaxy is demarcated by # characters.
#  There can be one or many stars in a given galaxy. Stars can only be in the shape of vowels { A, E, I, O, U }. A collection of * in
#  the shape of the vowels is a star. A star is contained in a 3×3 block. Stars cannot be overlapping. The dot(.) character denotes empty space.

# Given 3xN matrix comprising of { #, *, . } character, find the galaxy and stars within them.

# Note: Please pay attention to how vowel A is denoted in a 3×3 block in the examples section below.

 

# Constraints

# 3 <= N <= 10^5
# Input

# Input consists of a single integer N denoting the number of columns.
# Output

# The output contains vowels (stars) in order of their occurrence within the given galaxy. The galaxy itself is represented by the # character.

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

#   12

#   * . * # . * * * # . * .

#   * . * # . . * . # * * *

#   * * * # . * * * # * . *

#   Output

#   U#I#A

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