n=int(input())

for i in range(n,0,-1):
    for j in range(i,n):
        print(" ",end="")
    for k in range(2*i - 1):
        if k==0 or k==2*i - 2 or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()


