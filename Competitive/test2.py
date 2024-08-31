def sum1(n):
    ans = 0
    while (n>0):
        rem = n % 10
        ans += rem
        n = n//10
    return ans

def pro(n):
    ans = 1
    while(n>0):
        rem = n % 10
        ans = ans * rem
        n=n//10
    return ans

n=int(input())
flag = 1
if (n%2 == 0):
    print(sum1(n))
else:
    print(pro(n))
