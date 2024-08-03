def cal(m,n):
    ans=[]
    for i in range(m,n+1):
        if (i%3 ==0 and i%5==0):
            ans.append(i)
    return sum(ans)


print(cal(12,50))
print(cal(100,160))