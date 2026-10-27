class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # cool = 0
        # hold = 0
        # sell = 0


        # for num in prices:
        #     pcool = cool
        #     phold = hold
        #     psell = sell

        #     sell = max(hold - )
        #     cool = max(pcool, hold)
        #     hold = 
        

        hold = -prices[0]
        cool = 0 
        sell = 0
        for i in range(1, len(prices)):
            phold = hold

            hold = max(cool - prices[i], phold)
            cool = max(cool, sell)
            sell = prices[i] + phold
        return max(hold, sell, cool)



