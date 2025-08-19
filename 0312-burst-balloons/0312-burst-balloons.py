class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0,1)
        nums.append(1)
        dp = [[-1] *  (n+2) for _ in range(n+2)]

        def getAns(i,j):
            if i > j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            
            maxi = float('-inf')

            for ind in range(i,j+1):
                ans = nums[i-1] * nums[ind] * nums[j+1] + getAns(i, ind-1) + getAns(ind+1, j)
                maxi = max(ans,maxi)

            dp[i][j] = maxi
            return maxi

        return getAns(1,n)