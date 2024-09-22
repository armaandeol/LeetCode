class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        n = len(nums)
        for i in range(k):
            sum += nums[i]
        maxx = sum / k

        for i in range(k,n):
            sum += nums[i]
            sum -= nums[i-k]
            avg = sum / k
            maxx = max(maxx,avg)
        return maxx
        