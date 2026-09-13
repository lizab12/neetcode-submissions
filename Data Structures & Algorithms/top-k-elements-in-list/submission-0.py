class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        for n in nums:
            if n not in s:
                s[n]=1
            else:
                s[n]+=1
        s = sorted(s.items(), key = lambda x:x[1], reverse = True)
        return [item[0] for item in s[:k]]
        