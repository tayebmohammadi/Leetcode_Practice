class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        

        for amt in range(amount + 1):
            for coin in coins:
                if (amt - coin) < 0:
                    continue
                dp[amt] = min(dp[amt - coin] + 1, dp[amt])

        return dp[amount] if dp[amount] != float("inf") else  -1
        
                







































        # dp = [amount + 1] * (amount + 1)
        # dp[0] = 0

        # for i in range(1, amount + 1):

        #     for cn in coins:
        #         if i - cn >= 0:
        #             dp[i] = min(dp[i], (1 + dp[i - cn]))

        # return dp[amount] if dp[amount] != (amount + 1) else - 1








        