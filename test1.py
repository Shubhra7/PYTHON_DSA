t=2
text="bggbgbbg"
text1 = list(text)

for i in range(t):
    j=0
    while j<len(text1)-1:
        if(text1[j]=='b' and text1[j+1]=='g'):
            temp=text1[j]
            text1[j]=text1[j+1]
            text1[j+1]=temp
            j += 2
        else:
            j+=1

print("".join(text1))