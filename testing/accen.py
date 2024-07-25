

def check(s):
    ndig=0
    cap=0
    if(len(s)>=4):
        if not s[0].isdigit():
            for i in range(len(s)):
                if( s[i]==' ' or s[i]=='/'):
                    return 0
                if(s[i]>='A' and s[i]<='Z'):
                    cap+=1
                if s[i].isdigit():
                    ndig+=1
            if (cap >0 and ndig>0):
                return 1
        else:
            return 0
    else:
        return 0


print(check("aA1_67"))
print(check("a987 abC012"))
