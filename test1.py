input1 = "abc bcd cda"
input2 = "abc    bad"


in1, in2 = 0,0

for i in range(len(input1)):
    if(input1[i] == ' '):
        in1 += 1

for i in range(len(input2)):
    if(input2[i] == ' '):
        in2 += 1

val = abs(in1 - in2)
if(val%2 == 0):
    print("Even: ",val)
else:
    print("Odd: ",val)