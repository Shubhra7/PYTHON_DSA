# https://leetcode.com/problems/course-schedule-ii/
# https://youtu.be/WAOfKpxYHR8?si=BbchYSVSr6_aMbpt

"""
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
"""

from collections import deque
class Solution:
    ###########################
    # Same like topological sort
    ###########################
    def findOrder(self, numCourses: int, prerequisites):
        V=numCourses
        adj=[[] for _ in range(V)]
        indegree=[0]*V
        for u,v in prerequisites:
            adj[v].append(u)
        for i in range(V):
            for it in adj[i]:
                indegree[it]+=1
        q=deque()
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        topo=[]
        while q:
            ele=q.popleft()
            topo.append(ele)
            for subN in adj[ele]:
                indegree[subN]-=1
                if indegree[subN]==0:
                    q.append(subN)
        if len(topo)==V:
            return topo
        return []

obj=Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]  #[0, 1, 2, 3]
print(obj.findOrder(numCourses,prerequisites))
        