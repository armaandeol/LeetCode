class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[-1 for _ in range(2)] for _ in range(n)]

        def getAns(ind,buy):
            if ind >= n:
                return 0
            if dp[ind][buy] != -1:
                return dp[ind][buy]
            profit = 0
            if buy == 0:
                profit = max(0 + getAns(ind+1,0), -prices[ind] + getAns(ind+1,1)) 
            elif buy == 1:
                profit = max(0 + getAns(ind+1,1), prices[ind] + getAns(ind+2,0))

            dp[ind][buy] = profit
            return profit

        return getAns(0,0)