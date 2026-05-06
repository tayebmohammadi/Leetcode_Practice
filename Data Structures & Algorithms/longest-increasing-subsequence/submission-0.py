class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        lis = [1] * len(nums)

        for ind in range(len(nums) - 1, -1, -1 ):

            i = ind + 1
            while i < len(nums): 
                if nums[ind] < nums[i]:
                    lis[ind] = max(lis[ind], 1 + lis[i])
                i += 1

        return max(lis)

            



        