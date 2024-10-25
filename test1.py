def max_version(arr,n):
    maxi=-1
    for i in range(n):
        l=list(arr[i].split('_'))
        if (l[0]=='File' and l[1].isdigit()):
            if(maxi < int(l[1])):
                maxi = int(l[1])
    return maxi

n=4
arr1 = ["File_2","File_1","File_6","Fil_7"]
print(max_version(arr1,n))
arr = ["File_2","File_1","File_6s","Fil_7"]
print(max_version(arr,n))

