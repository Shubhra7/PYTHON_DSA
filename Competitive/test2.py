
# s="snakewatergunwater"
s="snakewaterwatergun"

a=[]
b=[]
flag=0

n=len(s)
word=""
for i in range(n):
    word += s[i]
    if(word=="snake" or word=="water" or word=="gun"):
        if(flag == 0):
            a.append(word[0])
            word=""
            flag=1
        else:
            b.append(word[0])
            word=""
            flag=0
# Each moves
# print(a)
# print(b)

A, B= 0,0
for i in range(len(a)):
    if (a[i]=='s' and b[i]=='w'):
        A += 1
    elif (a[i]=='w' and b[i]=='g'):
        A += 1
    elif (a[i]=='g' and b[i]=='s'):
        A += 1

print("A wins: ",A," times.")


    
    
    
        
    