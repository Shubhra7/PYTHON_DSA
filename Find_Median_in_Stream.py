from heapq import *
class Solution:
    def __init__(self):
        self.minHeap=[]
        self.maxHeap=[]
        
    def addNum(self,num):
        heappush(self.maxHeap,-num)
        heappush(self.minHeap,-heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap,-heappop(self.minHeap))
            
    def findMedian(self):
        if len(self.maxHeap)>len(self.minHeap):
            return -self.maxHeap[0]
        return (-self.maxHeap[0]+self.minHeap[0])/2
        
    def getMedian(self, arr):
        ans=[]
        for i in arr:
            self.addNum(i)
            ans.append(self.findMedian())
        return ans
obj=Solution()
arr=[5, 15, 1, 3, 2, 8]
print(obj.getMedian(arr))