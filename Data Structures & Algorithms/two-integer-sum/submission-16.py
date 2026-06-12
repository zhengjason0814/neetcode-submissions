class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in diff:
                return [diff[difference], i]
            diff[nums[i]] = i
