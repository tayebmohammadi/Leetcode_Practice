class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i  - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]

        









        # def fact(n):
        #     prod = 1
        #     for i in range(1,n + 1):
        #         prod *= i 

        #     return prod

        # numer = fact( m + n - 2)
        # denom = fact(m -1) * fact(n - 1)

        # return numer // denom

        