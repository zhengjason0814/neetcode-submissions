class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summed = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in summed:
                return [summed[difference],i]
            summed[nums[i]] = i