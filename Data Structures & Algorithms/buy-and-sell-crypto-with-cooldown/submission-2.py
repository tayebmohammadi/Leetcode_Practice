class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        hold = -prices[0]
        cool = 0 
        sell = 0
        for i in range(1, len(prices)):
            phold = hold

            hold = max(cool - prices[i], phold)
            cool = max(cool, sell)
            sell = prices[i] + phold
        return max(sell, cool)