class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        h = set()
        startIndex = 0
        endIndex = 0
        for i in range(len(s)):
            if s[i] in h:
                while s[i] in h:
                    h.remove(s[startIndex])
                    startIndex+=1
            h.add(s[i])
            endIndex +=1
            l = endIndex - startIndex
            if l>m:
                m = l
        return m
        