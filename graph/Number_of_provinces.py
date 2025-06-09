# https://leetcode.com/problems/number-of-provinces/description/

"""
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
"""

############################################
#               Optimal
############################################

class Solution:
    def findCircleNum(self, isConnected):
        n=len(isConnected)
        
        def dfs(start,visit):
            visit[start]=1
            for i in range(n):
                if isConnected[start][i]==1 and visit[i]==0:
                    dfs(i,visit)

        visit=[0]*n
        c=0
        for i in range(n):
            if visit[i]==0:
                c+=1
                dfs(i,visit)
        return c

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
obj=Solution()
print(obj.findCircleNum(isConnected))


#####################################################
#               Covert into ADJ matrix then do
#####################################################
class Solution:
    def findCircleNum(self, isConnected):
        def dfs(node,adjList,visit):
            visit[node]=1
            for j in adjList[node]:
                if visit[j]==0:
                    dfs(j,adjList,visit)
        v=len(isConnected)
        adjLis=[[] for _ in range(v)]
        for i in range(v):
            for j in range(v):
                if isConnected[i][j]==1 and i!=j:
                    adjLis[i].append(j)
                    # adjLis[j].append(i)
        # print(adjLis)
        cnt=0
        visit=[0]*v
        for i in range(v):
            if visit[i]==0:
                cnt+=1
                dfs(i,adjLis,visit)
        return cnt
        

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
obj=Solution()
print(obj.findCircleNum(isConnected))
        