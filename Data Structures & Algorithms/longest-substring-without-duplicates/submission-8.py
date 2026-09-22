class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a left and right pointer
        # run through the array, building a new string and dictionary
        # intialize a dictionary, using the character as the key and the index as the value
        # once run into a duplicate, store the index of the duplicate character as n + 1 and reset dictionary
        # also compare and store new max if it exceeds current max length
        # continue from new index

        left = 0
        counter = {}
        runningSum = 0

        for i in range(len(s)):
            if s[i] in counter and counter[s[i]] >= left:
                left = counter[s[i]] + 1
            counter[s[i]] = i
            runningSum = max(runningSum, i - left + 1)

        return runningSum
