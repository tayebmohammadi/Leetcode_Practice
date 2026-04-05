class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1] * length
        prod = 1
        for i in range(length):
            left[i] = prod
            prod *= nums[i]
        
        right = [1] * length
        prod = 1
        for j in range(length-1,-1,-1):
            right[j] = prod
            prod *= nums[j]
        result = [1] * length
        for k in range(length):
            result[k] = (left[k] * right[k])
        print(left)
        print(right)
        return result


            
            
        