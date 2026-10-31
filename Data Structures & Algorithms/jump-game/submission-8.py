class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # farthest = 0

        # for i in range(len(nums)):
        #     if i > farthest:
        #         return False
        #     if nums[i] + i > farthest:
        #         farthest = nums[i] + i
        #     if farthest >= len(nums) - 1:
        #         return True

        # return False

        gas = nums[0]

        for i in range(1, len(nums)):

            if gas == 0:
                return False
            gas = max(gas - 1, nums[i])
            

        return True
            
        