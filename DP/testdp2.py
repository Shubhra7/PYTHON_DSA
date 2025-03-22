
class Solution:
    def f(self,pat,lps):
        i,j=1,0
        n=len(pat)
        while i<n:
            if pat[i]==pat[j]:
                j+=1
                lps[i]=j
                i+=1
            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
    def search(self, pat, txt):
        # code here
        lps=[0]*len(pat)
        self.f(pat,lps)
        res=[]
        n,m=len(txt),len(pat)
        i,j=0,0
        while i<n:
            if pat[j]==txt[i]:
                j+=1
                i+=1
                if j==m:
                    res.append(i-j)
                    j=lps[j-1]
            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return res

obj=Solution()
print(obj.search("ab","abcab"))