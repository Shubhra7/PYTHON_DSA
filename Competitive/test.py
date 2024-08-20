Y = [[12,7],
    [4 ,5],
    [3 ,8]]

ans = Y[::-1]
for i in ans:
    print(i)



res = [[Y[j][i] for j in range(len(Y))]for i in range(len(Y[0]))]

for i in range(len(res)):
    res[i]=res[i][::-1]


for i in res:
    print(i)