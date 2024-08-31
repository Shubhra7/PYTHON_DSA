n=int(input())

p=0
for i in range(1,n):
    for k in range(i,n):
        print(" ",end="")
    print("*",end="")
    if((i+p) > 1):
        for j in range(i+p-2):
            print(" ",end="")
        print("*",end=" ")
    p += 1
    print()
    # print("hi")
for k in range(n+p):
    print("*",end="")