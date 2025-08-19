class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        count = len(cuts)
        dp = [[-1] * (count + 1) for _ in range(count+1)]

        cuts = [0]  + cuts + [n]

        cuts.sort()

        def getAns(i,j):
            if i > j :
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            mini = float('inf')
            
            for ind in range(i,j+1):
                ans = cuts[j+1] - cuts[i-1] + getAns(i,ind -1) + getAns(ind+1,j)
                mini = min(mini,ans)

            dp[i][j] = mini
            return mini

        return getAns(1,count)