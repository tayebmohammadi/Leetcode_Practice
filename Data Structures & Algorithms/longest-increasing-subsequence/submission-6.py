class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1] * n

        for right in range(n - 1, -1, -1):
            for left in range(right + 1, n):
                if nums[right] < nums[left]:
                    LIS[right] = max(LIS[left] + 1, LIS[right])
        return max(LIS)


        # lis = [1] * len(nums)

        # for ind in range(len(nums) - 1, -1, -1 ):
        #     for i in range(ind + 1, len(nums)): 
        #         if nums[ind] < nums[i]:
        #             lis[ind] = max(lis[ind], 1 + lis[i])

        # return max(lis)

            



        