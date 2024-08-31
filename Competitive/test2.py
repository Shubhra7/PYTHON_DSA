n=int(input())
for i in range(n):
    print("*",end="")
print()
for j in range(n-2):
    print('*',end="")
    for i in range(n-2):
        print(" ",end="")
    print('*')

for i in range(n):
    print("*",end="")