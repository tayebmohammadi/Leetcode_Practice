class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # small = prices[0]

        # for i in prices:
        #     if i < small:
        #         small = i
        #     profit = max(i - small, profit)
    
        # return profit        

        prof = 0
        small = prices[0]

        for price in prices:

            if price < small:
                small = price
            if (price - small) > prof:
                prof = price - small 
            
        return prof