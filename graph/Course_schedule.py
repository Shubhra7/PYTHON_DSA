# https://leetcode.com/problems/course-schedule/description/
# https://youtu.be/WAOfKpxYHR8?si=BbchYSVSr6_aMbpt

"""
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
"""


from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        #######################
        # Like topological Sort
        #######################
        V=numCourses
        adj=[[] for _ in range(V)]
        for u,v in prerequisites:
            adj[v].append(u)
        indegree=[0]*V
        for i in range(V):
            for it in adj[i]:
                indegree[it]+=1
        q=deque()
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        cnt=0
        while q:
            ele=q.popleft()
            cnt+=1
            for subN in adj[ele]:
                indegree[subN]-=1
                if indegree[subN]==0:
                    q.append(subN)
        if cnt==V:
            return True
        return False
    
numCourses = 2
# prerequisites = [[1,0],[0,1]]  # False
prerequisites = [[1,0]] #True
obj=Solution()
print(obj.canFinish(numCourses,prerequisites))
        