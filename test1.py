def A_Wins(s):
    word=""
    a,b=[],[]
    flag=0
    for i in range(len(s)):
        word+= s[i]
        if(word == "snake" or word == "water" or word == "gun"):
            if(flag == 0):
                a.append(word[0])
                flag=1
            else:
                b.append(word[0])
                flag=0
            word=""
    ans=0
    for i in range(len(a)):
        if (a[i]=='s' and b[i]=='w') or (a[i]=='w' and b[i]=='g') or (a[i]=='g' and b[i]=='s'):
            ans += 1
    
    return ans


s="snakewatergunsnake"
print("A wins: ",A_Wins(s)," times.")
print()

s1="snakesnakewatergun"
print("A wins: ",A_Wins(s1)," times.")