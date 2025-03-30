# https://youtu.be/QbwltemZbRg
# https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

"""
Input: deadline[] = [4, 1, 1, 1], profit[] = [20, 10, 40, 30]
Output: [2, 60]
Explanation: Job1 and Job3 can be done with maximum profit of 60 (20+40)
"""

class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        temp=[[deadline[i],profit[i]] for i in range(len(deadline))]
        n=len(deadline)
        maxdead=max(deadline)
        hashi=[-1]*(maxdead+1)
        temp.sort(key=lambda x:x[1],reverse=True)
        totalprofit=0
        count=0
        for i in range(n):
            for j in range(temp[i][0],0,-1):
                if hashi[j]==-1:
                    hashi[j]=i
                    totalprofit+=temp[i][1]
                    count+=1
                    break
        return [count,totalprofit]
obj=Solution()
print(obj.jobSequencing([4, 1, 1, 1],[20, 10, 40, 30]))  #o/p=>[2,60]