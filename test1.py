arr=list(input())
vol="aeiou"
ans=""
for i in arr:
    if i not in vol:
        ans+=i
print(ans)
