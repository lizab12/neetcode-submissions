class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for s in strs:
            key = [0]*26
            for char in range(len(s)):
                key[ord(s[char])-ord('a')]+=1
            key = tuple(key)
            if key in h:
                h[key].append(s)
            else:
                h[key]=[s]
        return list(h.values()) 
        