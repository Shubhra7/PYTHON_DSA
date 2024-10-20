text = "hello.hubhrajit.name.is.shubhrajit"

maxi = 0
ans=""

j=0
for i in range(1,len(text)):
    if(text[i] == '.'):
        val = i - j
        if(maxi < val):
            maxi = val
            ans = text[j:i]
            # print(ans)
        j=i+1
val = i - j + 1
# print(val)
if(maxi < val):
    ans = text[j:i+1]

print(ans)

