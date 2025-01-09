class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isValid(divisor):
            return sum(math.ceil(num / divisor) for num in nums) <= threshold

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if isValid(mid):
                right = mid 
            else:
                left = mid + 1

        return left