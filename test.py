# Link: https://youtu.be/XdbPH2tfXF4?t=594&si=M8yYELjQbm-ZCEJZ

# Boys would be behind the girls in t time which condition will get

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