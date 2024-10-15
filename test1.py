dice=4
num=1234
arr=list(str(num))

sum=0
if(dice % 2==0):
    for i in range(1,len(arr),2):
        sum += int(arr[i])
else:
    for i in range(0,len(arr),2):
        sum += int(arr[i])

print(sum)



