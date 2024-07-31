''' Program to transpose a matrix using list comprehension'''
### **** Good method ****

X = [[12,7],
    [4 ,5],
    [3 ,8]]


r = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
# print(r)



### *** Second Method ***

Y = [[12,7],
    [4 ,5],
    [3 ,8]]

ans=[[0 for i in range(len(Y))] for j  in range(len(Y[0]))]

for i in range(len(Y)):
    for j in range(len(Y[0])):
        ans[j][i]=Y[i][j]

print("Rotate matrix by 90 degree anticlockwise: ")
print(ans[::-1])

print("Rotate matrix by 90 degree clockwise: ")
for i in range(len(ans)):
    ans[i]=ans[i][::-1]
print(ans)
