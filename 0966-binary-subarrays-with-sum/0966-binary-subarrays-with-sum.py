class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(goal):
            if goal < 0:
                return 0
            left, right, summ, count = 0, 0, 0, 0
            while right < len(nums):
                summ += nums[right]
                while summ > goal:
                    summ -= nums[left]
                    left += 1
                count += (right - left + 1)
                right += 1
            return count
        return atMost(goal) - atMost(goal - 1)
