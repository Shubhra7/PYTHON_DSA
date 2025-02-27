# Python program to find length of the 
# longest valid substring 

def maxLength(s):
    maxLen=0
    l=[-1]
    for i in range(len(s)):
        if s[i]=='(':
            l.append(i)
        else:
            l.pop()
            if len(l)==0:
                l.append(i)
            else:
                maxLen=max(maxLen,i-l[-1])
    return maxLen

if __name__ == "__main__":
    s = ")()())"  #o/p =4
    print(maxLength(s))