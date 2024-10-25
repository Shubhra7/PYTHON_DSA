def A_Wins(s):
    i=0
    j=1
    word=""
    A,B =[],[]
    for i in range(len(s)):
        word += s[i]
        if(word == 'snake' or word=='water' or word=='gun'):
            if(j==1):
                A.append(word[0])
                j *= -1
            elif(j==-1):
                B.append(word[0])
                j *= -1
            word=""
    Ac=0
    for i in range(len(A)):
        if(A[i]=='s' and B[i]=='w') or (A[i]=='w' and B[i]=='g') or (A[i]=='g' and B[i]=='s'):
            Ac += 1
    return Ac
 

s="snakewatergunsnake"
print("A wins: ",A_Wins(s)," times.")
print()
s1="snakesnakewatergun"
print("A wins: ",A_Wins(s1)," times.")