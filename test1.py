def isgoogly(n):
    sum=0
    while n>0:
        rem = n %10
        sum = sum +rem
        n =n //10
    if(isprime(sum)):
        return True
    else:
        return False

def isprime(n):
    if(n<3 and n>0):
        return True
    elif(n>3):
        if(((n**2)-1) % 24 ==0):
            return True
    return False

n=141
if(isgoogly(n)):
    print("Yes")
else:
    print("No")