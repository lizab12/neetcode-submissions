class MedianFinder:

    def __init__(self):
        self.small, self.large = [],[]
        

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, num*-1)
        if len(self.large)>len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val*-1)
        elif len(self.large)<len(self.small):
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        if len(self.large)>len(self.small):
            return self.large[0]
        elif len(self.large)<len(self.small):
            return -1*self.small[0]
        else:
            return (-1*self.small[0]+self.large[0])/2
        
        