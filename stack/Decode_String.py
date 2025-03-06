# https://youtu.be/E9qHRcQXmDk?si=F5Hg01BTrFN7T0tY
# https://leetcode.com/problems/decode-string/description/

"""
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
"""
class Solution:
    def decodeString(self, s: str) -> str:
        num_stack=[]
        string_stack=[]
        k=0
        for c in s:
            if c.isdigit():
                k=(k*10)+int(c) #For handling more than one number as together like 12
                continue
            if c=='[':
                num_stack.append(k)
                k=0
                string_stack.append(c)
                continue
            if c!=']':
                string_stack.append(c)
                continue
            temp=[]
            while string_stack and string_stack[-1]!='[':
                temp.append(string_stack.pop())
            #remove the "["
            string_stack.pop()
            #Get the string
            count=num_stack.pop()
            replacement=''.join(reversed(temp))*count
            # Add it to the string
            string_stack.append(replacement)

        return ''.join(string_stack)

obj=Solution()
print(obj.decodeString("3[a]2[bc]"))