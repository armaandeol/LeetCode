class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            left = 0
            count = 0
            oddcount = 0  
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    oddcount += 1
                while oddcount > k:
                    if nums[left] % 2 == 1:
                        oddcount -= 1
                    left += 1
                count += (right - left + 1)
            return count

        return atMost(k) - atMost(k - 1)