text = "hello.hubhrajit.name.is.shubhrajit"

count = 0
ans = ""
maxi=0
j=0
for i in range(len(text)):
    if(text[i] == '.'):
        print(i," ",j)
        val = (i-j)
        if(val > maxi):
            maxi = val
            ans = text[j:i]
        j=i+1
print(i," ",j)
val = (i-j)+1   # beacuse in python the i will stop at last value not exceed 
print(val)
if(val > maxi):
    maxi=val
    ans = text[j:i+1]

print(maxi)
print(ans)



