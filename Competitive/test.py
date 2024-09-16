def checkPrime(l,i):
    for i in range(len(l)):
        p=

d = int(input())
p = int(input())

n = d//p

l=[0 for i in range(p)]
print(l)

val=1
for i in range(p):
    l[i] += val
    val += n

print(l)

val=1
for i in range(n):
    checkPrime(l,i)
