class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['[', '(', '{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                par = stack.pop()
                if par + c not in ['[]', '()', '{}']:
                    return False
        
        return len(stack) == 0