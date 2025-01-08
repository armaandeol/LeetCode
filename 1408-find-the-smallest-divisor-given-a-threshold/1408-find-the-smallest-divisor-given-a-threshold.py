class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isValid(divisor):
            return sum(math.ceil(num / divisor) for num in nums) <= threshold

        l, r = 1, max(nums) 
        while l < r:
            mid = (l + r) // 2
            if isValid(mid):
                r = mid 
            else:
                l = mid + 1

        return l