class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for s in strs:
            s1 = ("").join(sorted(s))
            if s1 in h:
                h[s1].append(s)
            else:
                h[s1]=[s]
        return list(h.values()) 
        