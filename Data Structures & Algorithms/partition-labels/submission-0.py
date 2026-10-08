class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = {}
        for i in range(len(s)):
                h[s[i]]=i
        size = 0
        end = 0
        output = []
        for i in range(len(s)):
            end = max(end, h[s[i]])
            size+=1
            if end == i:
                output.append(size)
                size, end = 0,0
        return output
        