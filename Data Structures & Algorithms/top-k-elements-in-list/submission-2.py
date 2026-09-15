class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1

        # most_freq = sorted(
        #     list(freq.keys()),
        #     key = lambda number: freq[number],
        #     reverse= True
        # )

        # res = []

        # for i in range(k):
        #     res.append(most_freq[i])
        # return res

        count = [[] for i in range(len(nums) + 1)]
        for num, cnt in freq.items():
            count[cnt].append(num)

        res = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res
            









            



