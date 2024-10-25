s2="bbkallalu"
s1="abbkalllup"

l1 = list(s1)
l1.sort()

l2 = list(s2)
l2.sort()

if("".join(l1) == "".join(l2)):
    print("Yes")
else:
    print("No")

