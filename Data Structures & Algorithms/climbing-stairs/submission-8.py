class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1

        prev1 = prev2 = 1
        for _ in range(2, n + 1):
            prev1, prev2 = prev1 + prev2, prev1
        return prev1


































        # res = {}

        # def dfs(n):
        #     if n < 4 :
        #         return n
            

        #     if n - 1 not in res:
        #         res[n - 1] = dfs(n - 1)
        #     if n - 2 not in res:
        #         res[n - 2] = dfs(n - 2)
            
        
        #     res[n] =  res[n - 1] + res[n - 2]
        #     return res[n]
        
        # return dfs(n)
