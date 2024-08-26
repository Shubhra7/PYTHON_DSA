
def all_prime_print(n):
    prime = [True for i in range(n)]
    # As 0 and 1 are not prime
    prime[0], prime[1] = False, False
    print(prime)
    for i in range(2,n):
        if(i*i > n):
            break
        if(prime[i]):
            # Mark all multiples of p as false (not prime)
            for j in range(i*i,n,i):
                prime[j]=False
    for k in range(2,n):
        if(prime[k]):
            print(k,end=" ")


n = int(input())
all_prime_print(n)