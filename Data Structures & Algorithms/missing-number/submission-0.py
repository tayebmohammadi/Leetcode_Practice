class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        curr = sum(nums)
        total = n * (n + 1) // 2

        return total - curr

        
        