def win_joshep(n,k):
    if(n==1):
        return 0
    else:
        return (((win_joshep(n-1,k))+k)%n)


print(win_joshep(41,2)+1)
print(win_joshep(5,3)+1)
print(win_joshep(1,3)+1)