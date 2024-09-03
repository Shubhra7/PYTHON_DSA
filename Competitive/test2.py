n=4
arr = ["File_2","File_1","File_6","Fil_7"]
maxi = -1
for i in range(len(arr)):
    l=list(arr[i].split('_'))
    if(len(l)==2 and l[1].isdigit() and l[0]=='File'):
        maxi=max(maxi, int(l[1]))
        p = "_".join(l)
    
print(maxi)
print(p)
