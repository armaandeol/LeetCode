class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxi = []
        for i in range(len(nums)):
            sum += nums[i]
            maxi.append(sum)
            if sum < 0:
                sum = 0
        return max(maxi)