class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        for num in nums:
            if num not in dup:
                dup[num] = 1
            else:
                dup[num] += 1
            if dup[num] > 1:
                return True
        return False