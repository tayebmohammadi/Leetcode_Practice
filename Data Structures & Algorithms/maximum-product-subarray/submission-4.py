class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        mn = mx = 1

        for num in nums:
            mx, mn = max(num, mn * num, mx * num), min(num, mn * num, mx * num)
            maxProd = max(maxProd, mx)
        return maxProd
                





































        
        # minP = 1
        # maxP = 1
        # great = max(nums)

        # for i in nums:
            
        #     tmp = maxP * i
        #     maxP = max(maxP * i, i, minP * i)
        #     minP = min(tmp, i, minP * i)
        #     great = max(great, maxP)


        # return great
            

            