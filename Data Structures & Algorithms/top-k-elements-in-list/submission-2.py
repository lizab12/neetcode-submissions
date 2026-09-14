class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        heap = []

        for num,freq in h.items():
                heapq.heappush(heap,(-freq,num))
        m = []
        for i in range(k):
            i,j = heapq.heappop(heap)
            m.append(j)
        return m
            