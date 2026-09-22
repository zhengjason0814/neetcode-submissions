class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        leftSegment = self.binarySearch(0, left - 1 if left > 0 else len(nums) - 1, nums, target)
        rightSegment = self.binarySearch(left, len(nums) - 1, nums, target)

        if leftSegment == None and rightSegment == None:
            return -1
        elif leftSegment == None:
            return rightSegment
        else:
            return leftSegment

    def binarySearch(self, left, right, nums, target):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return None
    