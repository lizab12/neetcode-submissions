class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cT, wT = {}, {}
        for i in t:
            if i not in cT:
                cT[i]=1
            else:
                cT[i]+=1
        have, need = 0, len(cT)
        res, resLen = [-1,-1], float("infinity")
        l = 0
        for i in range(len(s)):
            if s[i] not in wT:
                wT[s[i]]=1
            else:
                wT[s[i]]+=1
            if s[i] in cT and cT[s[i]]==wT[s[i]]:
                have+=1
            while have==need:
                if (i - l +1)<resLen:
                    resLen = i-l+1
                    res = [l,i]
                wT[s[l]]-=1
                if s[l] in cT and cT[s[l]]>wT[s[l]]:
                    have-=1
                l+=1
        return s[res[0]:res[1]+1]
        