class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set()
        for i in nums:
            h.add(i)
        l = 0
        l1 =0
        for i in h:
            if i-1 not in h:
                l1=1
                while i+1 in h:
                    l1+=1
                    i+=1
            if l1>l:
                l = l1
        return l

        