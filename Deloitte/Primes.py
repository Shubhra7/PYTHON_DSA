def isprime(val):
    if val<=1:
        return False
    if val>3:
        if ((val**2)-1)%24!=0:
            return False
    return True

n=input("Enter the input: ")   # 23==> 2, 3, 23 ;; 19=>19 ;; 40==>no prime found
ans=set()
for i in range(len(n)):
    for j in range(i,len(n)):
        val=int(n[i:j+1])
        if isprime(val):
            ans.add(val)
if len(ans)==0:
    print("No prime numbers found")
else:
    for i in ans:
        print(i,end=" ")




