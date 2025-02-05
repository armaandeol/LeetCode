class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(goal):
            if goal < 0:
                return 0
            l, r, summ, count = 0, 0, 0, 0
            while r < len(nums):
                summ += nums[r]
                while summ > goal:
                    summ -= nums[l]
                    l += 1
                count += (r - l + 1)
                r += 1
            return count
        return atMost(goal) - atMost(goal - 1)
