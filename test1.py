n=int(input("Enter the distance: "))
area = 3.14*n*n

val = area - int(area)

if(val > 0.5):
    ans = int(area)+1
else:
    ans = int(area)

print("The answer is: ",ans)