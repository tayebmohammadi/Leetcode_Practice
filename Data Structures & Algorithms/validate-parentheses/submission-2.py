class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        paran = {']': '[', '}': '{', ')': '(' }
        
        for c in s:
            if c in '({[':
                stack.append(c)
            elif c in paran:
                if not stack or stack.pop() != paran[c]:
                    return False

        return not stack