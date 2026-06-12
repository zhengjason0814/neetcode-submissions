class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        for i in range(len(nums)):
            if nums[i] not in dup:
                dup[nums[i]] = 1
            else:
                return True
        return False