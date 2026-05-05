class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        minP = 1
        maxP = 1
        great = max(nums)

        for i in nums:
            
            tmp = maxP * i
            maxP = max(maxP * i, i, minP * i)
            minP = min(tmp, i, minP * i)
            great = max(great, maxP)


        return great
            

            