text = "hello.hubhrajit.name.is.shubhrajit"

l=list(text.split('.'))
print(l)

maxi=""
for i in l:
    if(len(i) > len(maxi)):
        maxi=i
print(maxi)