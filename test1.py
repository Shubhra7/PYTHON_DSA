def isprime(n):
    if(n<=3):
        return True
    else:
        if(((n**2)-1)%24 == 0):
            return True
        return False

num = 92
arr=list(str(num))
sum=0
for i in arr:
    sum += int(i)
if(isprime(sum)):
    print("yes")
else:
    print("no")