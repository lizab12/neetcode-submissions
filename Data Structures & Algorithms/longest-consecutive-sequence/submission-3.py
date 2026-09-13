class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        h = set(nums)
        m = -1
        for num in h:
            if (num-1) not in h:
                l = 1
                while (num+l) in h:
                    l+=1
                m = max(m,l)
        return m

        