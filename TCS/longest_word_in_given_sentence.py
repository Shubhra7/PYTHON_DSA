sen="Hello Shubhrajit bubai Elephjansdjad"
maxi=0
li=sen.split()
ans=""
for i in li:
    if len(i)>maxi:
        maxi=len(i)
        ans=i
print(ans)