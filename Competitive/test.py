
def NumOfCar(num1,num2):
    carry=0
    count=0
    while (num1 != 0 or num2!=0):
        n1 = num1 % 10
        n2 = num2 % 10
        val = n1 + n2 + carry
        if (val > 9):
            carry = val // 10
            count += 1
        num1 , num2 = num1 // 10, num2 // 10
    return count

print(NumOfCar(451,349))
print(NumOfCar(23,563))