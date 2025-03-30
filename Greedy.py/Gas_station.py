# https://youtu.be/lJwbPZGo05A
# https://leetcode.com/problems/gas-station/description/

"""
Input: gas[] = [4, 5, 7, 4], cost[]= [6, 6, 3, 5]
Output: 2
Explanation: It is possible to travel around the circuit from station at index 2.
 Amount of gas at station 2 is (0 + 7) = 7.
Travel to station 3. Available gas = (7 – 3 + 4) = 8.
Travel to station 0. Available gas = (8 – 5 + 4) = 7.
Travel to station 1. Available gas = (7 – 6 + 5) = 6.
Return to station 2. Available gas = (6 – 6) = 0.
"""
class Solution:
    def startStation(self, gas, cost):
        # Your code here
        if sum(gas)<sum(cost):
            return -1
        total=0
        start=0
        for i in range(len(gas)):
            total+= gas[i]-cost[i]
            if total<0:
                total=0
                start=i+1
        return start
    
obj=Solution()
print(obj.startStation([4, 5, 7, 4],[6, 6, 3, 5]))  #O/P=2