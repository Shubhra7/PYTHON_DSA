dice=3
num=str(1234)

if(dice % 2==0):
    j=0
else:
    j=1

sum=0
for i in range(j,len(num),2):
    sum += int(num[i])

print(sum)