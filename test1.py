Stone = "BBBR"
INS= "RRRBGBRBBB"

ind =0
for i in range(len(Stone)):
    if(Stone[i] == INS[ind]):
        ind +=1

print(ind+1)
    