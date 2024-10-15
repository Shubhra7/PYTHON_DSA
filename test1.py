s1,s2 = "adventure","fadvenuture"
row = len(s2)
col = len(s1)
d=[[0 for i in range(col+1)]for j in range(row+1)]
maxi=0
ro,co =0,0
for i in range(1,row+1):
    for j in range(1,col+1):
        if(s2[i-1] == s1[j-1]):
            d[i][j] = d[i-1][j-1]+1
            if(maxi < d[i][j]):
                maxi = d[i][j]
                ro,co = i,j
        else:
            d[i][j] = 0

for i in d:
    print(i)
ans=""
i=0
while(i<maxi):
    ans = s2[ro-i-1] + ans
    i +=1
print(ans)
