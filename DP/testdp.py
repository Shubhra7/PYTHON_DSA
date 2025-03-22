class Solution:
    def f(self,s):
        n=len(s)
        lps=[0]*n
        i,j=1,0
        while i<n:
            if s[i]==s[j]:
                j+=1
                lps[i]=j
                i+=1
            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return lps[-1]
    def minInsertions(self, s: str) -> int:
        a=s+'#'+s[::-1]
        print(a)
        ans=self.f(a)
        return len(s)-ans
        
obj=Solution()
print(obj.minInsertions("zzazz"))