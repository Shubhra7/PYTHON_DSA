text= "hello.worlkopliad.from.shubhrajit"

ans=""
l=list(text.split('.'))
maxi=0
for i in l:
    if len(i) > maxi:
        maxi=len(i)
        ans=i

print(maxi)
print(ans)