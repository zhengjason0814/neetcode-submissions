class Solution:
    def trap(self, height: List[int]) -> int:
        # Make an array that stores the highest left height of current index
        # Make an array that stores the highest right height of current index
        # Make an array that stores the minimum height left or right of current index
            # Alternatively, I can just compute both min and sum as I iterate through each index
        # Then, iterate through, adding to the sum and return the sum

        length = len(height)
        maxLeft = [0] * length
        maxRight = [0] * length
        sum = 0

        for i in range(length):
            if i == 0:
                maxLeft[i] = height[i]
            else:
                maxLeft[i] = max(maxLeft[i - 1], height[i])
        
        for i in range(length - 1, -1, -1):
            if i == length - 1:
                maxRight[i] = height[i]
            else:
                maxRight[i] = max(maxRight[i + 1], height[i])

        for i in range(length):
            current = min(maxRight[i],maxLeft[i]) - height[i]
            if current > 0:
                sum += current
        return sum
