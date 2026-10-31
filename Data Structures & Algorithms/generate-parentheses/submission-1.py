class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        stack = []
        left, right = 0, 0
        res = []

        def backtrack(left, right):
            if left == n and right == n:
                string = "".join(stack)
                res.append(string)
                return
            
            if left < n:
                stack.append("(")
                backtrack(left + 1, right)
                stack.pop()
            if right < left:
                stack.append(")")
                backtrack(left, right + 1)
                stack.pop()
            
            return

        backtrack(0, 0)
        return res



            

            

            
             








































        # res = []
        # stack = []

        # def backtrack(openN,closedN):
        #     if openN == closedN == n:
        #         res.append("".join(stack))
        #         return 
            
        #     if openN < n:
        #         stack.append("(")
        #         backtrack(openN+1, closedN)
        #         stack.pop()
            
        #     if closedN < openN:
        #         stack.append(")")
        #         backtrack(openN, closedN+1)
        #         stack.pop()
        # backtrack(0,0)
        # return res

            

        