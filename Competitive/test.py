s=input()
ans=""
count=0
for i in range(len(s)):
    if (s[i] == '-'):
        count +=1
    else:
        ans += s[i]

print('-'*count + ans)