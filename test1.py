def isprime(n):
    if(n>1 and n<=3):
        return True
    else:
        if((n**2)-1)%24 == 0:
            return True
    return False

def prime_index_sum(arr,n):
    sum=0
    for i in range(2,len(arr)):
        if(isprime(i)):
            sum += arr[i]
    return sum


arr =[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n=10
print(prime_index_sum(arr,n))
