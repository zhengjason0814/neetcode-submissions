class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        length, anchor = len(nums), 0
        nums.sort()

        while anchor < length - 2:
            l = anchor + 1
            r = length - 1
            while l < r:
                if nums[anchor] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[anchor] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    triplets.append([nums[anchor], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            anchor += 1
            while nums[anchor] == nums[anchor - 1] and anchor < length - 2:
                anchor += 1

        return triplets
