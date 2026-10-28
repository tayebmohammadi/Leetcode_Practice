class Solution:
    def kClosest(self, nums: List[List[int]], k: int) -> List[List[int]]:
        if k > len(nums):
            return nums

        def quickSelect(left,right):
            if left >= right:
                return
            pivot = nums[right][0]**2 + nums[right][1]**2
            p = left

            for i in range(left, right):
                if (nums[i][0]**2 + nums[i][1]**2) < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[right], nums[p] = nums[p], nums[right]
                
            if p == k:
                return 
            elif p < k:
                quickSelect(p + 1, right)
            else:
                quickSelect(left, p - 1)

        quickSelect(0, len(nums) - 1)
        return nums[:k]









            






        



































        ## the heap stores the k points closet to the origin. 
        ## we need to calculate the distance of each points and update the heap accrodignly. 
        ## we can go uptpo k elemetns and heapify it. and the rest would cpamre to the heap root. 
        ## if the the distance is closer to the max heap we remove the root and put that instead. 
        ## should I use heap max or min? max bc i can easily tell if the new point is wihtin k closeset
        ## how to store the distance so that i donot recalcualte again and againe. 
        ## can i make a heap with tuples instead of intefers? 


        # heap = []

        # for xi, yi in points:
        #     if k > 0:
        #         dist = - 1 * math.sqrt((xi)**2 + (yi)**2)
        #         heapq.heappush(heap, (dist, [xi, yi]))
        #         k -= 1
        #     else:
        #         dist = - 1 * math.sqrt((xi)**2 + (yi)**2)
        #         if dist > heap[0][0]:
        #             heapq.heappop(heap)
        #             heapq.heappush(heap, (dist, [xi,yi]))

        
        # res = []

        # for i, j in heap:
        #     res.append(j)

        # return res


        # heap = []

        # for point in points:
        #     dis = - 1 * ((point[0])** 2 + (point[1])**2)
        #     res[dis].append(point)

        #     heapq.heappush(heap, (dis, [point[0], point[1]]))

        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return [point for dist, point in heap]
                


        

        