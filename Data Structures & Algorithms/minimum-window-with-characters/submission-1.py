class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        left = 0
        have = 0
        required = len(need)

        result = ""
        minLen = float("inf")

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == required:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    result = s[left:right + 1]

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        return result