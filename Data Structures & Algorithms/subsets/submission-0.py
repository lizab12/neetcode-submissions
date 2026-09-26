class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        m = [[]]
        for num in nums:
            cur = []
            for sub in m:
                cur.append(sub + [num])
            m+=cur
        return m
    
        