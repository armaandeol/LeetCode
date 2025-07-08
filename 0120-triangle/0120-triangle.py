class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = triangle[n-1].copy()

        for i in range(n-2,-1,-1):
            for j in range(i+1):
                memo[j] = min(memo[j],memo[j+1]) + triangle[i][j]

        return memo[0]