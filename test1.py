def isprime(n):
    if(n==2 or n==3):
        return True
    if(n>3):
        if(((n**2)-1)%24)==0:
            return True
    return False

n=int(input("Enter the number: "))
arr = list(str(n))

sum=0
for i in arr:
    sum += int(i)

if(isprime(sum)):
    print("Yes")
else:
    print("No")