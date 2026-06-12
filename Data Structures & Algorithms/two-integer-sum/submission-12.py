class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for index in range(len(nums)):
            difference = target - nums[index]
            if difference in diff:
                return [diff[difference], index]
            diff[nums[index]] = index