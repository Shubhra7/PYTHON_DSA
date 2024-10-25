Stone = "RRRBGBRBBB"
INS= "BBBR"

id=0
for i in range(len(INS)):
    if(Stone[id] == INS[i]):
        id += 1
print(id+1)