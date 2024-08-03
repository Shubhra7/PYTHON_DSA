def CheckPass(s):
    if (len(s) >=4 ):
        if not s[0].isdigit():
            num=0
            cap=0
            for i in s:
                if (i.isdigit()):
                    num+=1
                if (i>='A' and i<='Z'):
                    cap+=1
                if (i==' ' or i=='/'):
                    return 0
            if (num>0 and cap>0):
                return 1
    return 0

s=input()
print(CheckPass(s))