# https://youtu.be/U3N_je7tWAs
# https://www.geeksforgeeks.org/problems/alien-dictionary/1

#modified with striver

from collections import deque
class Solution:
    def findOrder(self,words):
        # code here
        def toposort(k,adj):
            q=deque()
            indegree=[0]*k
            for i in range(k):
                for it in adj[i]:
                    indegree[it]+=1
            for i in range(k):
                if indegree[i]==0:
                    q.append(i)
            ans=[]
            while q:
                ele=q.popleft()
                ans.append(ele)
                for it in adj[ele]:
                    indegree[it]-=1
                    if indegree[it]==0:
                        q.append(it)
            return ans
            
        N=len(words)
        unique_chars=set()
        for word in words:
            unique_chars.update(word)
        char_list=list(unique_chars)
        # SOME TIME not contigous so may make error out of the index
        char_to_index={ch:idx for idx,ch in enumerate(char_list)}
        index_to_char={idx:ch for idx,ch in enumerate(char_list)}
        k=len(char_list)
        
        adj=[[] for _ in range(k)]
        for i in range(N-1):
            st1,st2=words[i],words[i+1]
            length=min(len(st1),len(st2))
            for j in range(length):
                if st1[j] != st2[j]:
                    u = char_to_index[st1[j]]
                    v=char_to_index[st2[j]]
                    adj[u].append(v)
                    break
            else:
                # If no differing character and first word is longer than second
                if len(st1)>len(st2):
                    return ""
                
        topo=toposort(k,adj)
        if len(topo) !=k:
            return ""
        ans=""
        for it in topo:
            ans += index_to_char[it]
        return ans
    
obj=Solution()
wr=["bdbc" ,"dbe", "bcebc", "e", "bedb"]
print("ans: ")
print(obj.findOrder(wr))