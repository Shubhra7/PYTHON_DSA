arr=[1,6,0,-1,-2,3,4,8,6,4,3,2,1,0]
# arr=[1]

count=0
maxi=0
j=0
p=[]
for i in range(1,len(arr)):
    if(arr[i]<arr[i-1]):
        if arr[i-1] not in p:
            p.append(arr[i-1])
        p.append(arr[i])
        count += 1
        # maxi = max(maxi,count+1)
    else:
        maxi = max(maxi,count+1)
        count = 0
        j=i
    maxi=max(maxi,count+1)   #checking for last one also

print(maxi)
print(p[-maxi:len(p)])

