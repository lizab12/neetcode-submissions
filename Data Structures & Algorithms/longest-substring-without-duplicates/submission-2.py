class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        hashMap = {}
        start = 0
        max_len = 0

        for i in range(len(s)):
            if s[i] in hashMap:
                # move start forward only if needed
                start = max(start, hashMap[s[i]] + 1)

            hashMap[s[i]] = i
            l = i - start + 1
            max_len = max(max_len, l)

        return max_len
