text = "TeamATeamBTeamATeamBTeamATeamBTeamBTeamA"
 
i=4 
Aval, Bval = 0,0
while (i < len(text)):
    if(text[i]=='A'):
        Aval += 1
    else:
        Bval += 1
    i += 5

if(Aval > Bval):
    print("TeamA")
else:
    print("TeamB")