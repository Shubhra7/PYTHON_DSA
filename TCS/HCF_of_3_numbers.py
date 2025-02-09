def find_hcf(a,b):
    while b:
        a,b = b,a%b
    return a

l = [2, 4, 6, 8, 16]
num1,num2= l[0],l[1]
gcd=find_hcf(num1,num2)

for i in range(2,len(l)):
    gcd = find_hcf(gcd,l[i])

print("The gcd of the array is: ",gcd)
