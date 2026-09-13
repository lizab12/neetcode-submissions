class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        h = {}
        l = 0
        res = 0
        for i in range(len(s)):
            if s[i] in h:
                h[s[i]]+=1
            else:
                h[s[i]] = 1
            while (i-l+1) - max(h.values()) > k:
                h[s[l]]-=1
                l+=1
            res = max(res, i-l+1)
        return res
            
            