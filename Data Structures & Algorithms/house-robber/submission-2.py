class Solution:
    def rob(self, nums: List[int]) -> int:
        m = len(nums)

        if m == 1:
            return nums[0]

        if m == 2:
            return max([nums[0], nums[1]])

        rob = []
        rob.append(nums[0])
        rob.append(max(nums[0], nums[1]))

        for i in range(2,len(nums)):
            rob.append(max(nums[i] + rob[i - 2], rob[i - 1]))

        return max(rob[-1], rob[-2])
            