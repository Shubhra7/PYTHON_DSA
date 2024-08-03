s=input()
ans=int(s[0])
for i in range(1,len(s),2):
    if (s[i] == 'A'):
        ans &= int(s[i+1])
    elif (s[i] == 'B'):
        ans |= int(s[i+1])
    elif (s[i] == 'C'):
        ans ^= int(s[i+1])
    
print(ans)

