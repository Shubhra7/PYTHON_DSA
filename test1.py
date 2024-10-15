l=[]
def isprime(n):
    if(n==1):
        return False
    if(n==2 or n==3):
        return True
    elif((n**2)-1)%24==0:
        return True
    return False

def prime_index_sum(arr,n):
    sum=0
    for i in range(n):
        if(isprime(i)):
            sum += arr[i]
            l.append(arr[i])
    return sum

arr =[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n=10
print(prime_index_sum(arr,n))
print(l)