def covert(n):
    l=list(n.split('0'))
    ans=""
    for i in l:
        val = len(i)
        ans += chr(ord('A')-1+val)
    return ans


n=input("Enter the string: ")
print(covert(n))