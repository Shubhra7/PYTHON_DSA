arr=[1,6,0,-1,-2,3,4,8,6,4,3,2,1,0]

count = 0
p=[]
maxi=0
j=0
for i in range(1,len(arr)):
    if(arr[i]<arr[i-1]):
        if arr[i-1] not in p:
            print(arr[i-1],end=" ")
            p.append(arr[i-1])
        p.append(arr[i])
        print(arr[i],end=" ")
        count += 1
    else:
        print()
        maxi=max(maxi,count+1)
        count = 0
        j=i
if(maxi < count+1):
    maxi = count+1
    j=i
# maxi = max(maxi,count+1)
print()
print(maxi)
print(p)
print(p[-maxi:len(p)])
