def check_no(match, word):
    count = 0
    j,i = len(match)-1, len(word)-1
    while (j>=0 and i>=0 and match[j]==word[i]):
        count += 1
        j -= 1
        i -= 1
    return count

arr = list(input().split())
match = input()

print(arr)
ml=0
ans=""

for i in arr:
    cl = check_no(match,i)
    if( cl>ml or (cl == ml and len(i)<len(ans))):
        ml = cl
        ans = i
print(ans)
    