def mac(a,b):
    i,j = len(a)-1, len(b)-1
    count=0
    while(i>=0 and j>=0 and a[i]==b[j]):
        count += 1
        i-=1
        j-=1
    return count

arr = ["gender","blender","blunder","under"]
match = "thunder"

maxi=0
ans=""
for i in arr:
    val = mac(i,match)
    if(val > maxi):
        maxi = val
        ans = i
    if(val == maxi):
        if(len(i) < len(ans)):
            ans = i

print(maxi)
print(ans)
