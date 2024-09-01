arr = [4,5,7,2,15,20]
m=5


arr.sort()
t_can=0
for i in arr:
    if(i % 5 == 0):
        t_can += 1
    else:
        if(m>=i):
            t_can += 1
            m -= i
print(t_can)