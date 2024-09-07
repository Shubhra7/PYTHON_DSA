pass1 = "File_12"

l=list(pass1.split('_'))

if (l[0]=="File"):
    if(l[1].isdigit()):
        print(int(l[1]))
else:
    print(-1)