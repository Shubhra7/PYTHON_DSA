def max_version(arr1,n):
    maxi=-1
    for i in arr1:
        l=i.split('_')
        if(l[0]=='File' and l[1].isdigit()):
            if(int(l[1]) > maxi):
                maxi=int(l[1])
    return maxi



n=4
arr = ["File_2","File_1","File_6s","Fil_7"]
print(max_version(arr,n))