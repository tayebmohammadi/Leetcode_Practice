class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1)] * (m + 1)
        dp[m - 1][n - 1] = 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
        return dp[0][0]










        # dp = [[1] * n for _ in range(m)]

        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i  - 1][j] + dp[i][j - 1]
        
        # return dp[m - 1][n - 1]





        # def fact(n):
        #     prod = 1
        #     for i in range(1,n + 1):
        #         prod *= i 

        #     return prod

        # numer = fact( m + n - 2)
        # denom = fact(m -1) * fact(n - 1)

        # return numer // denom

        