def A_Wins(s):
    word=""
    valA = []
    valB =[]
    flag=0
    for i in s:
        word += i
        if(word=="snake" or word=="water" or word=="gun"):
            if(flag==0):
                valA.append(word[0])
                word=""
                flag=1
            else:
                valB.append(word[0])
                word=""
                flag=0
    A=0
    for i in range(len(valA)):
        if((valA[i]=='s' and valB[i]=='w') or
           (valA[i]=='w' and valB[i]=='g')or
           (valA[i]=='g' and valB[i]=='s')):
            A+=1
    return A

s="snakewatergunsnake"
print("A wins: ",A_Wins(s)," times.")
print()
s1="snakesnakewatergun"
print("A wins: ",A_Wins(s1)," times.")