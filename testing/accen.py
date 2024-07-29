
def CheckPassword(st):
    if (len(st) >= 4):
        if not st[0].isdigit():
            cap=0
            num=0
            for i in range(len(st)):
                if (st[i]==' ' or st[i]=='/'):
                    print("shubhra")
                    return 0
                if (st[i]>='A' and st[i]<='Z'):
                    cap+=1
                if (st[i].isdigit()):
                    num+=1
            if( cap>0 and num>0):
                return 1
        else:
            print("kalu1")
            return 0
    else:
        print("kalu1")
        return 0 

st="a987 abC012"
print(CheckPassword(st))