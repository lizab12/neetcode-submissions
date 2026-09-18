class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2==1:
            return False
        for i in s:
            if i == '[' or i== '(' or i=='{':
                stack.append(i)
            else:
                if not stack:
                    return False
                compare = stack[-1]
                if (i == ']' and compare == '[') or (i == ')' and compare == '(') or (i == '}' and compare == '{'):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        