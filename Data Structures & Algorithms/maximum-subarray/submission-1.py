class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_total = total = nums[0]

        for i in range(1, len(nums)):
            total = max(nums[i], nums[i] + total)
            max_total = max(max_total, total)
        
        return max_total








































        # maxTotal = nums[0]
        # previousbig = nums[0]

        # for i in range(1, len(nums)):

        #     maxTotal = max(maxTotal, nums[i], nums[i] + previousbig)
        #     previousbig = max(0,     nums[i], nums[i] + previousbig)

        # return maxTotal


            

        