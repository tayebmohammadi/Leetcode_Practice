class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxTotal = nums[0]
        previousbig = nums[0]

        for i in range(1, len(nums)):

            # if nums[i] + previousbig > maxTotal: 
            #     maxTotal += nums[i]


            maxTotal = max(maxTotal, nums[i], nums[i] + previousbig)
            previousbig = max(0,     nums[i], nums[i] + previousbig)

        return maxTotal


            

        