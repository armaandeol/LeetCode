class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum, rightSum = [0] * len(nums), [0] * len(nums)
        for i in range(len(nums)):
            leftSum[i] = sum(nums[:i])
            rightSum[i] = sum(nums[i+1:])

        return [abs(x - y) for x, y in zip(leftSum, rightSum)]

