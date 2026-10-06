class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, s):
            if i == len(nums):
                return 1 if s == target else 0

            if (i, s) in memo:
                return memo[(i, s)]

            memo[(i, s)] = (
                dfs(i + 1, s + nums[i]) +
                dfs(i + 1, s - nums[i])
            )

            return memo[(i, s)]

        return dfs(0, 0)