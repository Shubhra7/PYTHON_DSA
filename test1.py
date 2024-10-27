def mat(a,b):
    i,j = len(a)-1,len(b)-1
    count=0
    while (i>=0 and j>=0 and a[i]==b[j]):
        count+=1
        i-=1
        j-=1
    return count
arr = ['gender','blender','blunder','under']
match = 'thunder'

count=0
maxi=0
ans=""
for i in arr:
    count = mat(i,match)
    if(count > maxi):
        maxi=count
        ans=i
    if(count==maxi):
        if(len(ans) > len(i)):
            ans=i

print(maxi)
print(ans)