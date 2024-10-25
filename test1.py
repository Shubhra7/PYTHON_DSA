t=2
text1="bggbgbbg"
text = list(text1)

for _ in range(t):
    # for i in range(0,len(text)-1,):
    i=0
    while(i<len(text)-1):
        if(text[i]=='b' and text[i+1]=='g'):
            text[i], text[i+1] = text[i+1],text[i]
            i+=2
        else:
            i+=1
    print("".join(text))

print("".join(text))