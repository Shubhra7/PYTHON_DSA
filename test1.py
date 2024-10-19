x="niveditha"
y="lavekdahnita"
S,R = 3,5

# x="abcdef"
# y="pafedexycbc"
# S,R = 4,2

# x="gagu"
# y="kkkkkk"
# S,R = 4,2


stra = 0
revi =0
i=0
j=1
flag1,flag2 =0,0
ds,dr =0,0


while (j<len(x)):
    flag1,flag2 =0,0
    ds,dr =0,0
    val = x[i:j]
    print(val)
    if( val in y):
        if((j+1) in range(len(x)+1) and x[i:j+1] in y):
            print("exst==>",x[i:j+1])
            flag1=1
            # j+=1
            # continue
        ds = j - i
        # stra += 1
        # i=j
        # j+=1
    if(val[::-1] in y):
        # print("rev==>",x[i:j+1][::-1])
        if((j+1) in range(len(x)+1) and x[i:j+1][::-1] in y):
            print("exrev==>",x[i:j+1][::-1])
            flag2=1
            # j+=1
            # continue
        dr = j - i
        # revi += 1
        # i=j
        # j+=1
    if(flag1==1 or flag2==1):
        j += 1
        continue
    print("DOing")
    print(ds," ",dr)
    if(ds == dr and ds!=0 and dr!=0):
        if(S > R):
            # print("Huh")
            print("win==>rev")
            revi += 1
            i=j
            j+=1
        else:
            print("win==>str")
            stra += 1
            i=j
            j+=1
    elif(ds > dr):
        print("win==>str")
        stra += 1
        i=j
        j+=1
    elif(ds < dr):
        print("HUh")
        print("win==>rev")
        revi += 1
        i=j
        j+=1
    else:
        j += 1

print(ds," ",dr)
if(flag1 == 1):
    print("win==>str")
    stra += 1
    i=j
    j+=1
elif(flag2 == 1):
    print("win==>rev")
    revi += 1
    i=j
    j+=1
print(stra)
print(revi)
if(stra == 0 and revi == 0):
    print("Impossible")
else:
    ans = (stra*S) + (revi*R)
    print(ans)
