start = 3

n = int(input("Enter the row: "))
for i in range(1,n+1):
    ans=""
    for j in range(0,i):
        ans = str(start+j) + ans
    start += i
    print(ans)

pop = start
start -= 1
ans = ""
for i in range(n):
    ans = ans + str(start)
    start -= 1
print(ans)


count = pop - n - 1

for i in range(n-1,-1,-1):
    ans =""
    for j in range(i,0,-1):
        ans = ans + str(count)
        count -= 1
    print(ans)

