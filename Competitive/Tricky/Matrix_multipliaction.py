a=[[1,2,3],
   [1,2,1],
   [3,1,2]]

b=[[1,2,3],
   [1,2,1],
   [3,1,2]]

row,col=len(a),len(a[0])
sum=0
ans=[[0]*col for _ in range(row)]

arow,acols=len(a),len(a[0])
bcols=len(b[0])
for i in range(arow):
    for j in range(bcols):
        for k in range(acols):
            sum+=a[i][k]*b[k][j]
        ans[i][j]=sum
        sum=0

for i in ans:
    print(i)
