class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Intialize a dictionary, startingNum array, counter, and maxCounter
        # Pass through array once, putting all elements into the dictionary
            # key is the value, value is the index
        # For every key in the dictionary, we check if key - 1 is in the dict.
            # If key - 1 is not in the dict, we append to the dict
        # Then, for every num in startingNum array, we loop:
            # counter = 0
            # if num + 1 in dict, counter + 1
            # if not, check maxCounter and update
        # Finally return maxCounter

        numDict, startNum, counter, maxCounter = {}, [], 0, 0
        for i in range(len(nums)):
            numDict[nums[i]] = i
        for key in numDict.keys():
            if key - 1 not in numDict:
                startNum.append(key)
        print(startNum)
        for num in startNum:
            counter = 1
            j = num
            while j + 1 in numDict:
                counter += 1
                j += 1
            if maxCounter < counter:
                maxCounter = counter
        return maxCounter