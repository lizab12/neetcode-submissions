import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []

        for i in range(len(nums)):
            # negative because Python heapq is min-heap
            heapq.heappush(heap, (-nums[i], i))

            # remove elements outside the current window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            if i >= k - 1:
                result.append(-heap[0][0])

        return result