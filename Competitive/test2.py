n = int(input("Enter the number: "))

k=1
for i in range(n):
    for j in range(n):
        print(k,end="")
        if(j != n-1):
            print("*",end="")
        k += 1
    print()