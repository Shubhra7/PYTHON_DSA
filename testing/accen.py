s="1C0C1C1A0B1"
ans=int(s[0])
for i in range(1,len(s),2):
    if s[i]=='C':
        ans=ans ^ int(s[i+1])
    elif s[i]=='A':
        ans=ans & int(s[i+1])
    elif s[i]=='B':
        ans=ans | int(s[i+1])
print(ans)