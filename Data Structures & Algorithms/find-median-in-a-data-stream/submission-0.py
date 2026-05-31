class MedianFinder:

    def __init__(self):
        self.nums = []


        

    def addNum(self, num: int) -> None:

        for i in range(len(self.nums)):
            if self.nums[i] > num:
                self.nums.insert(i, num)
                return
        self.nums.append(num)


    def findMedian(self) -> float:
        n = len(self.nums)

        if n % 2:
            return self.nums[n//2]
        else:
            return (self.nums[n//2 - 1] + self.nums[n//2]) / 2
        
        