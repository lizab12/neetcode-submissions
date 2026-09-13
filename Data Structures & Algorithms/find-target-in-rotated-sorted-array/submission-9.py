class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        if len(nums)==1 and nums[0]==target:
            return 0
        if len(nums)==1 and nums[0]!=target:
            return -1
        if len(nums)<=5:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
        found = False
        while(l<=r):
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[r]<nums[mid] and nums[r]>target:
                l = mid + 1
            elif nums[l]>nums[mid] and nums[mid]<target:
                r = mid - 1
            elif nums[mid]>target:
                r = mid - 1
            elif nums[mid]<target:
                l = mid + 1
        if found == False:
            return -1
        