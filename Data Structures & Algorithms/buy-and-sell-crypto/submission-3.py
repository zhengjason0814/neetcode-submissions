class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        # Use two pointers, assuming the current index as the time to sell
        # If current index is lower than left pointer, move left pointer right
        # If left pointer is lower than the right pointer, move right pointer right
        left = 0
        right = 1
        while right < len(prices):
            if prices[right] < prices[left]:
                left += 1
                if left == right:
                    right += 1
            else:
                res = max(res,prices[right] - prices[left])
                right += 1


        return res

