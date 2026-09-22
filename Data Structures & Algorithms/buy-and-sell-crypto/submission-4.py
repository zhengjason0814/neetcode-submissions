class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        left, right = 0, 1

        while right < len(prices):
            if prices[right] <= prices[left]:
                left = right
                right += 1
            else:
                res = max(prices[right] - prices[left], res)
                right += 1

        return res

