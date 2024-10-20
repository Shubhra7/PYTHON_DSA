s1 = "abbkalllu"
s2="bbkallalu"

x, y = sorted(list(s1)), sorted(list(s2))
print(x)
print(y)
ans1 = "".join(x)
ans2 = "".join(y)

print(ans1," ",ans2)

if(ans2 == ans1):
    print("Yes")
else:
    print("No")