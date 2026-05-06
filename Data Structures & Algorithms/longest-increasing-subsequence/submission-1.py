class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        lis = [1] * len(nums)

        for ind in range(len(nums) - 1, -1, -1 ):
            for i in range(ind + 1, len(nums)): 
                if nums[ind] < nums[i]:
                    lis[ind] = max(lis[ind], 1 + lis[i])

        return max(lis)

            



        