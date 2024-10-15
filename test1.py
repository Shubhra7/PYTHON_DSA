text = "TeamATeamBTeamATeamBTeamATeamBTeamBTeamA"

Av = Bv =0

for i in range(4,len(text),5):
    if(text[i]=='A'):
        Av += 1
    else:
        Bv += 1

if(Av > Bv):
    print("TeamA")
else:
    print("TeamB")