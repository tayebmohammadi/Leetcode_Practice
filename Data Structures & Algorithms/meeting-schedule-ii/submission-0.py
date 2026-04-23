"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s = 0
        e = 0

        maxRoom = 0
        room = 0

        while s < len(start):
            if start[s] < end[e]:
                room += 1
                s += 1
            else:
                room -= 1
                e += 1
            
            
            maxRoom = max(room, maxRoom)

        return maxRoom
        
        
