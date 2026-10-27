class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        for r in range(len(text2) - 1, -1, -1):
            for c in range(len(text1) - 1, -1, -1):
                if text1[c] == text2[r]:
                    memo[r][c] = 1 + memo[r + 1][c + 1]
                else:
                    memo[r][c] = max(memo[r + 1][c], memo[r][c + 1])
        return memo[0][0]

        





































        # dp = [[0 for i in range(len(text2) + 1)] for j in range (len(text1) + 1)]


        # for m in range(len(text1) - 1, -1, -1):
        #     for n in range(len(text2) -1, -1, -1):
                
        #         if text1[m] == text2[n]:
        #             dp[m][n] = 1 + dp[m + 1][n + 1]

        #         else:
        #             dp[m][n] = max(dp[m][n + 1], dp[m + 1][n])
        
        # return dp[0][0]


        