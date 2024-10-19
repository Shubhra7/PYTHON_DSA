# x="niveditha"
# y="lavekdahnita"
# S,R = 3,5

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
    if( val in y):
        if((j+1) in range(len(x)+1) and x[i:j+1] in y):
            flag1=1
        ds = j - i
    if(val[::-1] in y):
        if((j+1) in range(len(x)+1) and x[i:j+1][::-1] in y):
            flag2=1
        dr = j - i
    if(flag1==1 or flag2==1):
        j += 1
        continue
    if(ds == dr and ds!=0 and dr!=0):
        if(S > R):
            revi += 1
            i=j
            j+=1
        else:
            stra += 1
            i=j
            j+=1
    elif(ds > dr):
        stra += 1
        i=j
        j+=1
    elif(ds < dr):
        revi += 1
        i=j
        j+=1
    else:
        j += 1

if(flag1 == 1):
    stra += 1
    i=j
    j+=1
elif(flag2 == 1):
    revi += 1
    i=j
    j+=1
if(stra == 0 and revi == 0):
    print("Impossible")
else:
    ans = (stra*S) + (revi*R)
    print(ans)
