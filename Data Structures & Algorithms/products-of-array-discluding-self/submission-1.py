class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zero = set()
        for i in range(len(nums)):
            if nums[i]==0:
                zero.add(i)
            else:
                p = p*nums[i]
        if len(zero)>=2:
            return [0]*len(nums)
        if len(zero)==1:
            for i in range(len(nums)):
                if i in zero:
                    nums[i]=p
                else:
                    nums[i]=0
            return nums
        if len(zero)==0:
            for i in range(len(nums)):
                nums[i]=int(p/nums[i])

            return nums
            
        