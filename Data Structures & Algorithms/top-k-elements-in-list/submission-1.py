class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = Counter(nums)
        heap = [(-f,n) for n,f in f_map.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range (k)]
        