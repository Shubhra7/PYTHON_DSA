def max_version(arr,n):
    maxi = -1
    for i in range(len(arr)):
        l=list(arr[i].split('_'))
        if(len(l)==2 and l[1].isdigit() and l[0]=='File'):
            maxi=max(maxi, int(l[1]))
    return maxi

n=4
arr1 = ["File_2","File_1","File_6","Fil_7"]
print(max_version(arr1,n))
arr = ["File_2","File_1","File_6s","Fil_7"]
print(max_version(arr,n))

