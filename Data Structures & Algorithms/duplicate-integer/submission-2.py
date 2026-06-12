class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for element in nums:
            if element not in dict:
                dict[element] = 1
            else:
                dict[element] += 1
            if dict[element] > 1:
                return True
        return False
         