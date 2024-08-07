def check(st):
    if (len(st) >= 6):
        sm=0
        cap=0
        no=0
        for i in st:
            if (i>='a' and i<='z'):
                sm+=1
            elif (i>='A' and i<='Z'):
                cap+=1
            elif (i==' ' or i=='/'):
                return "Invaild password"
            elif (i.isdigit()):
                no+=1
        if (no >1 and sm >0 and cap > 0):
            return "password valid"
    return "Invalid password"

st = input()
print(check(st))