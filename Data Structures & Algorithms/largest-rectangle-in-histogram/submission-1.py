class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for idx, height in enumerate(heights):
            start = idx
            while stack and height < stack[-1][1]:
                currHeight = stack[-1][1]
                length = idx - stack[-1][0]
                maxArea = max(maxArea, currHeight * length)
                start = stack[-1][0]
                stack.pop()
            stack.append([start, height])

        n = len(heights)
        while stack:
            curr = stack.pop()
            currHeight = curr[1]
            length = n - curr[0]
            maxArea = max(maxArea, currHeight * length)
        
        return maxArea