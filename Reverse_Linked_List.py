arr=[9,8,7,5,4,3,2,1,0,-1,-2,3,4,8,6,4,3,2,1,0]
# arr=[1,6,0,-1,-2,3,4,8,6,4,3,2,1,0]
# arr=[1]
j=0
count=0
maxi=0
l=[]

for i in range(1,len(arr)):
    if(arr[i] < arr[i-1]):
        count += 1
    else:
        if(maxi < count):
            maxi = count
            j=i-1
        count = 0
if(maxi < count):
    maxi = count
    j= len(arr)-1

print(maxi+1)
print(arr[j-maxi:j+1])