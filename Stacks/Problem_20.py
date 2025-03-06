class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {
            "(": ")",
            "{": "}",
            "[":"]"
        }

        for i in s:
            if(i not in opening and stack == []):
                return False
            if (i in opening):
                stack.append(i)
            else:
                if(i == opening[stack[-1]]):
                    stack.pop()
                else:
                    return False
            
        if (stack):
            return False
        return True