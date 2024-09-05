n=5
e=2
d=10
flag=0

count = 1
ava = n
l=[]
l.append(ava)
for i in range(1,d+1):
    if( ava >= e):
        ava -= e
        l.append(ava)
    else:
        if(i%7 != 0):
            ava += n
            count += 1
            ava -= e
            l.append(ava)
        else:
            print(-1)
            flag=1
            break
if(flag == 0):
    print(count)
print(l)

