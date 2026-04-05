class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = 1 + freq.get(i,0)

        temp_list =[]
        for key, value in freq.items():
            temp_list.append([value,key])
        temp_list.sort()

        result = []
        while k > 0:
            result.append(temp_list.pop()[1])
            k -= 1
        return result