class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s11 = [0]*26
        s22 = [0]*26
        left = 0
        for i in range(len(s1)):
            s11[ord(s1[i])-ord('a')]+=1
        for i in range(len(s2)):
            m = ord(s2[i])-ord('a')
            s22[m]+=1
            while s22[m]>s11[m]:
                leftIndex = ord(s2[left]) - ord('a')
                s22[leftIndex] -= 1
                left += 1
            if s11==s22:
                return True
        return False