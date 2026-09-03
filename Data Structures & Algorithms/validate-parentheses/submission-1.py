class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        Close_to_open={")":"(","]":"[","}":"{"}

        for c in s:
            if c in Close_to_open:
                if stack and stack[-1]== Close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False