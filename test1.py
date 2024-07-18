no1=list(map(int,input()))
no2=list(map(int,input()))
no3=list(map(int,input()))

l=[no1,no2,no3]
print(l)

ans=1
ans=min([i[2]] for i in l)[0]
ans=ans + min([i[1]] for i in l)[0]*10
ans=ans + min([i[0]] for i in l)[0]*100
ans=ans + max([max(no1),max(no2),max(no3)])*1000
print(ans)
