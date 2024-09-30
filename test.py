t=2
text1="bggbgbbg"
text = list(text1)

for i in range(t):
    j=0
    while j<len(text)-1:
        if(text[j]=='b' and text[j+1]=='g'):
            temp = text[j]
            text[j] = text[j+1]
            text[j+1] = temp
            j += 2
        else:
            j+=1

print(''.join(text))