class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_map = defaultdict(list)
        for word in strs:
            sort = ''.join(sorted(word))
            a_map[sort].append(word)
        return list(a_map.values())