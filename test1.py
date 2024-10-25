text = "TeamATeamBTeamATeamBTeamATeamBTeamATeamA"

Aval, Bval=0,0
i=4
for j in range(4,len(text),5):
    if(text[j]=='A'):
        Aval += 1
    if(text[j]=='B'):
        Bval += 1
if(Aval > Bval):
    print("TeamA")
else:
    print("TeamB")