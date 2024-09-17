import math
n = 505
prime_list = [True for i in range(n + 1)]
pr = 2
# Sieve of Eratosthenes 
while pr * pr <= n:    
    if prime_list[pr] == True:        
        for i in range(pr * 2, n + 1, pr):            
            prime_list[i] = False    
    pr += 1

prime_list[0] = False
prime_list[1] = False

d,p = map(int, (input().split()))
n = int(d / p)
count = 0
# as 0, 1 not prime so starting from 2
for i in range(2, n):    
    prime_time = True    
    for j in range(p):        
        num = i + j * n        
        if not prime_list[num]:            
            prime_time = False            
            break   
        # print("HI")
        print(num,end=" ")
    print() 
    if prime_time:        
            count += 1
print(count)