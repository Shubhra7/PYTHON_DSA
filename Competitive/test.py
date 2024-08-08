fName = input()
lName = input()

common = set(fName) & set(lName)

print(common)

s1_flit = "".join([x for x in fName if x in common])
s2_flit = "".join([x for x in lName if x in common])
print(s1_flit)
print(s2_flit)