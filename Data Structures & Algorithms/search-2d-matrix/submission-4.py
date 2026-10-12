class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                elif arr[mid] == target:
                    return True
                else:
                    right = mid - 1

            return False
        
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            if target > matrix[mid][0]:
                if mid == len(matrix) - 1:
                    return binarySearch(matrix[mid], target)
                if target < matrix[mid + 1][0]:
                    return binarySearch(matrix[mid], target)
                else:
                    left = mid + 1
            elif target < matrix[mid][0]:
                if mid == 0:
                    return binarySearch(matrix[mid], target)
                if target > matrix[mid - 1][0]:
                    return binarySearch(matrix[mid - 1], target)
                else:
                    right = mid - 1
            else:
                return True

        return False