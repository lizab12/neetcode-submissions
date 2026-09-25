import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for i in points:
            dist = (i[0]*i[0] + i[1]*i[1])
            heapq.heappush(h, (dist,i))
        l = []
        for i in range(k):
            m,point = heapq.heappop(h)
            l.append(point)
        return l