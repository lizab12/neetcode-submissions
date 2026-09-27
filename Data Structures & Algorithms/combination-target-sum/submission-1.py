class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        m = []

        def dfs(i, cur, s):
            if s == target:
                m.append(cur.copy())
                return

            if i == len(nums) or s > target:
                return

            # Take nums[i]
            cur.append(nums[i])
            dfs(i, cur, s + nums[i])

            # Backtrack
            cur.pop()

            # Don't take nums[i], move to next number
            dfs(i + 1, cur, s)

        dfs(0, [], 0)
        return m