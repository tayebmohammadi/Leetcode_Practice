class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        j = len(numbers) - 1
        result = []
        while i<= j:
            total = numbers[i] + numbers[j]
            if total == target:
                result.append(i+1)
                result.append(j+1)
                return result
            elif total < target:
                i += 1
            else:
                j -= 1
        return result
        
        
        