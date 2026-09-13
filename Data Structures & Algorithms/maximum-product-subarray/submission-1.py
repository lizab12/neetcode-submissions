from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_max = curr_min = result = nums[0]

        for n in nums[1:]:
            if n < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(n, curr_max * n)
            curr_min = min(n, curr_min * n)

            result = max(result, curr_max)

        return result
