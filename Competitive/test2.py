n = int(input("enter no.of rows: "))

for i in range(n):
    for k in range(i,n-1):
        print(" ",end="")
    for l in range(2*i + 1):
        print("*",end="")
    print()
for i in range(n-1,-1,-1):
    for k in range(i,n):
        print(" ",end="")
    for l in range(2*i - 1):
        print("*",end="")
    print()

