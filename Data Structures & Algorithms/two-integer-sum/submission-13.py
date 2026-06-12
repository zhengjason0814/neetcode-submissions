class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffDict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in diffDict:
                return [diffDict[difference], i]
            diffDict[nums[i]] = i

        