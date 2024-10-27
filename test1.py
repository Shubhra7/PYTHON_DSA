def solve_dec(arr):
    count = 0
    maxi=0
    ro=0
    for i in range(1,len(arr)):
        if(arr[i] < arr[i-1]):
            count += 1
        else:
            if(maxi < count):
                maxi = count
                ro = i-1
            count = 0
    if(count > maxi):
        maxi = count
        ro = i
    print(ro)
    print(maxi+1)
    print(arr[ro-maxi:ro+1])
    

arr=[1,6,0,-1,-2,3,4,8,6,4,3,2,1,0]
# arr=[1]
# arr=[9,8,7,5,4,3,2,1,0,-1,-2,3,4,8,6,4,3,2,1,0]
solve_dec(arr)