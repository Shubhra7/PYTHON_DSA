from collections import Counter

def anargram_check(s1,s2):
    p=Counter(s1)
    print(p)
    for i in s2:
        if(i not in p.keys()):
            return False
        p[i] = p.get(i)  - 1

    print(p)
    ans = 0
    for i in p.values():
        ans += i

    if(ans == 0):
        return True
    else:
        return False

s1 = "abbkalllu"
s2="bbkallalu"
print(anargram_check(s1,s2))

