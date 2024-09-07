
l = [1,2,3,4,1,2,0,1,2,3]
print(len(l))

sum = 0
for i in range(0,len(l),2):
    sum += l[i]

print(sum)