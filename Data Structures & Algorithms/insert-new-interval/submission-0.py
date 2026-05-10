class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        
        for int in range(len(intervals)):

            if newInterval[1] < intervals[int][0]:
                res.append(newInterval)
                return res + intervals[int:]

            elif newInterval[0] > intervals[int][1]:
                res.append(intervals[int])

            elif intervals[int][0] <= newInterval[0] <=  intervals[int][1] or intervals[int][0] <= newInterval[1] <=  intervals[int][1]:
                newInterval = [min(intervals[int][0], newInterval[0]), max(intervals[int][1], newInterval[1])]

            
        res.append(newInterval)

        return res


                

        
        