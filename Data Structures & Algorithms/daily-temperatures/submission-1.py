class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result = [0] * len(temperatures)
        # stack = []

        # for i,t  in enumerate(temperatures):
        #     while stack and t > stack[-1][0]:
        #         stackT, stackInd = stack.pop()
        #         result[stackInd] = i - stackInd
        #     stack.append([t,i])
        # return result

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                ind, tem = stack[-1]
                res[ind] = i - ind
                stack.pop()

            stack.append([i,t])
        return res







