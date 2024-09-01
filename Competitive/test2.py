

def divident_pos(arr, divisior, quotinet, rem):
    ans = (divisior*quotient)+rem
    if ans in arr:
        return arr.index(ans)
    else:
        return -1

arr = [5,6,7,9,10]
divisior = 2
quotient = 3
rem = 1

print(divident_pos(arr, divisior, quotient, rem))