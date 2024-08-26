
def all_prime_print(n):
    prime = [True for i in range(n)]
    prime[0], prime[1] = False, False
    print(prime)
    for i in range(2,n):
        if(i*i > n):
            break
        if(prime[i]):
            for j in range(i*i,n,i):
                prime[j]=False
    for k in range(2,n):
        if(prime[k]):
            print(k,end=" ")


n = int(input())
all_prime_print(n)