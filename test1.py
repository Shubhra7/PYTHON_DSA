# n=2
# mat1=[list(map(int,input().split()))for i in range(n)]
# print(mat1)
# print("Enter the second matrix: ")
# mat2=[list(map(int,input().split())) for i in range(n)]
# dp=[[0]*2 for _ in range(2)]
# for i in range(2):
#     for j in range(2):
#         sumi=0
#         for k in range(2):
#             sumi+=mat1[i][k]*mat2[k][j]
#         dp[i][j]=sumi
# for i in dp:
#     print(i)

a=['1','2','3']
p=list(map(int,a))
print(type(p[1]))