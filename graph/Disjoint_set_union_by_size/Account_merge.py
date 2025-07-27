# https://www.geeksforgeeks.org/problems/merging-details/1
# https://youtu.be/FMwpt_aQOGw?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn

"""
Input: 
n: 5
details = 
[["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: 
[["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
"""

# Check duplicate and make DSU
# then merge

from typing import List
from collections import defaultdict

class DisjoinSet:
    def __init__(self, V):
        self.size = [1 for _ in range(V)]
        self.parent = [i for i in range(V)]
        
    def findUPar(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.findUPar(self.parent[u])
        return self.parent[u]
        
    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] > self.size[ulp_v]:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
        else:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]

class Solution:
    def mergeDetails(self, details: List[List[str]]) -> List[List[str]]:
        n = len(details)
        ds = DisjoinSet(n)
        mail_to_index = {}

        # Step 1: Map mails to users and do unions
        for i in range(n):
            for j in range(1, len(details[i])):
                mail = details[i][j]
                if mail not in mail_to_index:
                    mail_to_index[mail] = i
                else:
                    ds.unionBySize(i, mail_to_index[mail])
        
        # Step 2: Group mails by their ultimate parent
        merged = defaultdict(list)
        for mail, idx in mail_to_index.items():
            parent = ds.findUPar(idx)
            merged[parent].append(mail)
        
        # Step 3: Prepare final answer
        result = []
        for parent_idx, mails in merged.items():
            name = details[parent_idx][0]
            result.append([name] + sorted(mails))
        
        return result
    
n=5
details = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]

obj=Solution()
print(obj.mergeDetails(details))