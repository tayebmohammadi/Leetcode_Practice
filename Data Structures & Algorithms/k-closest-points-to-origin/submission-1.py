class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        ## the heap stores the k points closet to the origin. 
        ## we need to calculate the distance of each points and update the heap accrodignly. 
        ## we can go uptpo k elemetns and heapify it. and the rest would cpamre to the heap root. 
        ## if the the distance is closer to the max heap we remove the root and put that instead. 
        ## should I use heap max or min? max bc i can easily tell if the new point is wihtin k closeset
        ## how to store the distance so that i donot recalcualte again and againe. 
        ## can i make a heap with tuples instead of intefers? 


        heap = []

        for xi, yi in points:
            if k > 0:
                dist = - 1 * math.sqrt((xi)**2 + (yi)**2)
                heapq.heappush(heap, (dist, [xi, yi]))
                k -= 1
            else:
                dist = - 1 * math.sqrt((xi)**2 + (yi)**2)
                if dist > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (dist, [xi,yi]))

        
        res = []

        for i, j in heap:
            res.append(j)

        return res
                


        

        