t=2
text1="bggbgbbg"
l = list(text1)

for i in range(t):
    j=1
    while j < len(l):
        if(l[j]=='g' and l[j-1]=='b'):
            l[j], l[j-1] = l[j-1],l[j]
            j += 2
        else:
            j += 1

print("".join(l))