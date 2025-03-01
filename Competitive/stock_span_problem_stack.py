class Solution:
    def __init__(self):
        self.stack=[]
    def check(self,val):
        span=1
        while self.stack and self.stack[-1][0]<=val:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([val,span])
        return span
    def calculateSpan(self, arr):
        #write code here
        res=[]
        for i in range(len(arr)):
            res.append(self.check(arr[i]))
        return res

obj=Solution()
ans=obj.calculateSpan([100,80,60,70,60,75,85])
print(*ans) # unpacked operator
