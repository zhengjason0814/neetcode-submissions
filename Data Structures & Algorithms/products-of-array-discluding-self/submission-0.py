class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            product = 1
            for index in range(len(nums)):
                if index == i:
                    continue
                else:
                    product *= nums[index]
            answer.append(product)
        return answer