import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for i in stones:
            heapq.heappush(h,i*-1)
        while h:
            m1 = heapq.heappop(h)
            if not h:
                return abs(m1)
            m2 = heapq.heappop(h)
            if(abs(m1-m2)!=0):
                heapq.heappush(h, abs(m1-m2)*-1)


        return 0
        