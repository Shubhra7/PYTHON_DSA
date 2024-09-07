def fact(n):
    if(n==1):
        return 1
    else:
        val = 1
        for i in range(1,n+1):
            val *= i 
        return val

text = "abbcep"
l = ['a','e','i','o','u','A','E','I','O','U']
d={}
Ccount = 0

for i in text:
    if i not in l:
        d[i]=d.get(i,0)+1
        Ccount += 1

req = 1
for i in d.values():
    if (i>1):
        req = req * fact(i)

print(Ccount)
print("The permutaion result is: ",fact(Ccount)/req)