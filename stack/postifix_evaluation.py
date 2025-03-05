class Solution:
    def evaluate(self, arr):
        # code here
        stack=[]
        for i in range(len(arr)):
            if arr[i].lstrip('-').isdigit():
                stack.append(arr[i])
            else:
                val1,val2 = int(stack.pop()),int(stack.pop())
                if arr[i]=='+':
                    val2=val2+val1
                if arr[i]=='-':
                    val2=val2-val1
                if arr[i]=='/':
                    val2=int(val2/val1)
                if arr[i]=='*':
                    val2=val2*val1
                stack.append(str(val2))
        return stack[-1]
obj=Solution()
st="-8 3 /" #o/p => -2
arr=list(st.split(" "))
print(obj.evaluate(arr))
