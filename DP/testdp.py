def maxLen(arr):
    # code here
    one,zero=0,0
    maxi=0
    for i in range(len(arr)):
        if arr[i]==1:
            one += 1
        if arr[i]==0:
            zero += 1
        print(one," ",zero)
        if one == zero:
            print("HI")
            maxi=one
    return maxi

print(maxLen([1,0,1,1,1,0,0]))