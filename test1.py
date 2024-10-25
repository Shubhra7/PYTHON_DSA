def prime_index_sum(arr,n):
    sum=0
    for i in range(len(arr)):
        if(isprime(i)):
            print(arr[i])
            sum += arr[i]
    return sum

def isprime(n):
    if(n>1 and n<=3):
        return True
    elif(n>3):
        if(((n**2)-1)%24==0):
            return True
    return False


arr =[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n=10
print(prime_index_sum(arr,n))
# print(l)