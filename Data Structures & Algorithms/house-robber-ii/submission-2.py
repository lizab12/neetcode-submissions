class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2 or len(nums)==3:
            return max(nums)
        max1 = 0
        first1, first2 = nums[0], nums[1]
        second1, second2 = max(nums[0], nums[1]), max(nums[1], nums[2])
        for i in range(2, len(nums)-1):
            max1 = max(nums[i]+first1, second1)
            first1 = second1
            second1 = max1
            print(max1)
        max2 = 0
        for i in range(3, len(nums)):
            max2 = max(nums[i]+first2, second2)
            first2 = second2
            second2 = max2
            print(max2)
        return max(max1, max2)
        
            
        