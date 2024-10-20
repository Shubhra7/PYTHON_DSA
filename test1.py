def isprime(n):
    if(n==2 or n==3):
        return True
    if(n>3):
        if((n**2)-1)%24==0:
            return True
    return False
def sum_prime_index(arr):
    ans=0
    for i in range(len(arr)):
        if(isprime(i)):
            ans += arr[i]
    return ans


arr =[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(sum_prime_index(arr))