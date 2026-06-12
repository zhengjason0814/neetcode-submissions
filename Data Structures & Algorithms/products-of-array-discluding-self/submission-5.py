class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Prefix array calculation
        n = len(nums)
        left, right, answer = [1] * n, [1] * n, [1] * n

        left[0] = nums[0]
        for i in range(1,n):
            left[i] = nums[i] * left[i - 1]

        # Suffix array calculation
        right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = nums[i] * right[i + 1]

        for i in range(n):
            if i > 0:
                prefix_val = left[i - 1]
            else:
                prefix_val = 1
            if i < n - 1:
                suffix_val = right[i + 1]
            else:
                suffix_val = 1
            answer[i] = prefix_val * suffix_val
        return answer


        