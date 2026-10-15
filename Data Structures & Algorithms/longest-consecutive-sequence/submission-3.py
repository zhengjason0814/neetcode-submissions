class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            numSet.add(num)
        
        startingNum = []
        for num in numSet:
            if num - 1 not in numSet:
                startingNum.append(num)

        maxLength = 0
        for num in startingNum:
            counter, j = 1, num
            while j + 1 in numSet:
                counter += 1
                j += 1
            maxLength = max(maxLength, counter)

        return maxLength
            
            