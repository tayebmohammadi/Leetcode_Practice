class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        res = self.permute(nums[1:])
        ans = []
        for perm in res:  
            print(perm)
            for i in range(len(perm) + 1):
                perm_copy = perm.copy()
                perm_copy.insert(i, nums[0])
                ans.append(perm_copy)
        return ans


