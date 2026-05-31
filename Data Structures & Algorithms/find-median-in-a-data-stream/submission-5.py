class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # make sure the every num in small <= evry num in large
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # make sure the small is not bigger than large
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return ((self.large[0] + (-1 * self.small[0])) / 2 )
        
    


    # def __init__(self):
    #     self.nums = []




    # def addNum(self, num: int) -> None:

    #     for i in range(len(self.nums)):
    #         if self.nums[i] > num:
    #             self.nums.insert(i, num)
    #             return
    #     self.nums.append(num)


    # def findMedian(self) -> float:
    #     n = len(self.nums)

    #     if n % 2:
    #         return self.nums[n//2]
    #     else:
    #         return (self.nums[n//2 - 1] + self.nums[n//2]) / 2
        
        