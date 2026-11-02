class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, val in enumerate(temperatures):
            while stack and temperatures[idx] > stack[-1][1]:
                numDays = idx - stack[-1][0]
                res[stack[-1][0]] = numDays
                stack.pop()
            stack.append([idx,val])
        
        return res