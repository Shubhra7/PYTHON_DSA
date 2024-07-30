
def NumberOfCarries(num1,num2):
    carry=0
    c=0
    while num1!=0 or num2!=0:
        val=(num1%10) + (num2%10) + carry
        if val > 9:
            carry = val // 10
            c+=1
        num1 = num1 //10
        num2 = num2 //10
    return c
        




num1=451
num2=349
print(NumberOfCarries(num1,num2))
print(NumberOfCarries(23,563))