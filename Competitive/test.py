import collections

def check(s):
    p=[]
    for i in range(len(s)):
        if (s[i]=='[' or s[i]=='{' or s[i]=='('):
            p.append(s[i])
        else:
            if (len(p) == 0):
                return False
            val = p.pop()
            if (s[i]==']' and val != '['):
                return False
            elif (s[i]=='}' and val != '{'):
                return False
            elif (s[i] == ')' and val != '('):
                return False
    return True


s="[({)}]"
print(check(s))