
def OptBin(st):
    ans=int(st[0])
    for i in range(1,len(st),2):
        if st[i] == 'A':
            ans=ans & int(st[i+1])
        elif st[i] == 'B':
            ans=ans | int(st[i+1])
        elif st[i] == 'C':
            ans = ans ^ int(st[i+1])
    return ans


st="1C0C1C1A0B1"
print(OptBin(st))

kalu="0C1A1B1C1C1B0A0"
print(OptBin(kalu))