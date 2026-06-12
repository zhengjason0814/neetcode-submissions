class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summed = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in summed:
                return[summed[diff],i]
            summed[nums[i]] = i


        