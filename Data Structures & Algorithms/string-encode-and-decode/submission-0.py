class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s+=i
            s+="."
        return s

    def decode(self, s: str) -> List[str]:
        s1=[]
        s2=""
        for i in s:
            if i == ".":
                s1.append(s2)
                s2=""
            else:
                s2+=i
        return s1
