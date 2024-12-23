class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mpp = defaultdict(int)
        summ = 0
        count = 0

        mpp[0] = 1
        for i in range(n):

            summ += nums[i]
            remove = summ - k
            count += mpp[remove]

            mpp[summ] += 1

        return count