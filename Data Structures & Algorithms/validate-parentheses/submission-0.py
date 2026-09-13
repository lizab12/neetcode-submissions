class Solution:
    def isValid(self, s: str) -> bool:
        s1 = []
        n = len(s) - 1
        while n >= 0:
            if s[n] == '[' and s1 and s1[-1] == ']':
                s1.pop()
            elif s[n] == '(' and s1 and s1[-1] == ')':
                s1.pop()
            elif s[n] == '{' and s1 and s1[-1] == '}':
                s1.pop()
            else:
                s1.append(s[n])
            n -= 1

        return not s1
