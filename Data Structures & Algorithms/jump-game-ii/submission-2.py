class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l = r = 0
        farthest = 0
        count = 1
        for i in range(1, len(nums) - 1):
            for l in range(l, r + 1):
                farthest = max(farthest, nums[l] + l)
                if farthest >= len(nums) - 1:
                    return count
            l, r = r + 1, farthest
            count += 1
        
        return count


