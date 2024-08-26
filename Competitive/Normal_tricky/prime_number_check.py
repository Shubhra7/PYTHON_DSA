n=int(input())

if( n==0 or n==1):
    print("Not Prime")
elif( n==2):
    print("Prime")
else:
    if(n>3):
        if((n**2)-1)%24 != 0:
            print("Not Prime")
        else:
            print("Yes prime")
