class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, curSum = nums[0], 0
        for n in nums:
            if curSum<0:
                curSum = 0
            curSum+=n
            if curSum>maxSum:
                maxSum = curSum
        return maxSum
        