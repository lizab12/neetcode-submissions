class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        left= 0
        result= 0
        maxfreq = 0 
        for i in range(len(s)):
            if s[i] in h:
                h[s[i]]+=1
            else:
                h[s[i]] = 1
            maxfreq = max(maxfreq, h[s[i]])
            while (i-left+1)-maxfreq >k:
                h[s[left]]-=1
                left+=1
            result = max(result, i - left + 1)
        return result


        