import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.kk = k
        for i in nums:
            heapq.heappush(self.heap,i)
        while len(self.heap)>k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        m = -1
        while len(self.heap)>=self.kk:
            m = heapq.heappop(self.heap)
        heapq.heappush(self.heap,m)
        return m
