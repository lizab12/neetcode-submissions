class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = {}
        for i in nums:
            if i not in h:
                h[i]=1
            else:
                return i
        return -1
        