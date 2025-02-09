from HCF_of_3_numbers import find_hcf

def lcm_of_array(arr):
    lcm=arr[0]  #****
    for i in range(1,len(arr)):
        num1=lcm
        num2=arr[i]
        gcd=find_hcf(num1,num2)
        lcm=(lcm*arr[i])//gcd #*** important
    return lcm

arr1=[1,2,8,3]
arr2 = [2, 7, 3, 9, 4]
print(lcm_of_array(arr1))
print(lcm_of_array(arr2))