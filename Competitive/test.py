def longestValidParentheses(s):
        if len(s)==0:
            return 0
        li=[]
        ans=0
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                li.append(s[i])
            else:
                if(len(li)!=0):
                    val = li.pop()
                    if(s[i]==')' and val=='('):
                        ans=i
                    if(s[i]=='}' and val=='{'):
                        ans=i
                    if(s[i]==']' and val=='['):
                        ans=i
            print(li)
        return ans

print(longestValidParentheses("(()"))