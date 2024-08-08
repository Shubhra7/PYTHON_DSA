def lcs(x,y):
    m=len(x)
    n=len(y)

    L = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j] = 0
            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
                print(y[i-1])
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    for i in L:
        print(i)

    return L[m][n]


fName = input()
lName = input()

common = set(fName) & set(lName)

print(common)

s1_flit = "".join([x for x in fName if x in common])
s2_flit = "".join([x for x in lName if x in common])
# print(s1_flit)
# print(s2_flit)
# print(min(s1_flit,s2_flit,key=len))

print(lcs(fName,lName))

