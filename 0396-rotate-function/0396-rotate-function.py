class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        total = sum(nums)
        current = sum(i * num for i, num in enumerate(nums))

        answer = current

        for k in range(1, n):
            current = current + total - n * nums[-k]
            answer = max(answer, current)

        return answer