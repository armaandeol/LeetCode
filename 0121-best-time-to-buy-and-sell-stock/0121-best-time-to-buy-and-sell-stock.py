class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maxprofit = 0
        n = len(prices)
        for i in range(n):
            cost = prices[i] - minimum
            maxprofit = max(maxprofit, cost)
            minimum = min(minimum, prices[i])

        return maxprofit