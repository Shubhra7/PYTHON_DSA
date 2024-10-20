text = "TeamATeamBTeamATeamBTeamATeamBTeamBTeamATeamA"

Aval , Bval =0,0

i=0
while(i<len(text)):
    if(text[i] == 'A'):
        Aval += 1
        i += 5
    elif(text[i] == 'B'):
        Bval += 1
        i += 5
    else:
        i+=1
print(Aval, " ",Bval)
if(Aval > Bval):
    print("TeamA")
else:
    print("TeamB")
    

    