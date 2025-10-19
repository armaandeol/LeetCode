class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        cur = float('-inf')
        count = 0
        
        for num in nums:
            cur = max(cur, num - k)
            if cur <= num + k:
                count += 1
                cur += 1
        
        return count