class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        ans = 1
        longest = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif nums[i] + 1 == nums[i + 1]:
                ans += 1
            else:
                ans = 1

            longest = max(longest, ans)

        return longest