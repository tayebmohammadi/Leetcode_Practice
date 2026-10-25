class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[0] = 1

        if n < 2:
            return n
        

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] +  dp[i - 2]
        
        return dp[n]


































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
