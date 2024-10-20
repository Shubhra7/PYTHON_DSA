def do(arr):
    j=0
    maxi =0
    val=0
    p=[]
    for i in range(1,len(arr)):
        if(arr[i]<arr[i-1]):
            val += 1
        else:
            if(val > maxi):
                maxi=val
                j=i-1
            val =0
    
    if(val > maxi):
        j=i
        maxi = val
    print(maxi + 1)
    kalu = arr[j-maxi:j+1]
    print(kalu)



# arr=[1,6,0,-1,-2,3,4,8,6,4,3,2,1,0]
arr=[7,5,2,-1,-2,-3,0,1,2,3,4,8,7,6,5,4,3,1]
do(arr)