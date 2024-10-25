def divident_pos(arr,divi,quo,rem):
    val = (divi * quo)+rem
    if(val in arr):
        return arr.index(val)
    else:
        return -1

arr = [5,6,7,9,10]
divisior = 2
quotient = 3
rem = 1

print(divident_pos(arr, divisior, quotient, rem))