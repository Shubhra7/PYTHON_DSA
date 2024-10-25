arr=[9,8,7,5,4,3,2,1,0,-1,-2,3,4,8,6,4,3,2,1,0]
# arr=[1,6,0,-1,-2,3,4,8,6,4,3,2,1,0]
# arr=[1]
count =0
i=1
maxi=0
while i< len(arr):
    if(arr[i] < arr[i-1]):
        count += 1
    else:
        if count > maxi:
            maxi = count
            ro=i
        count = 0
    i += 1

if(count > maxi):
    maxi=count
    ro=len(arr)

print("val---")
print(maxi)
print(ro)
print(ro-maxi-1," ",ro)
print(arr[ro-maxi-1:ro])
    
