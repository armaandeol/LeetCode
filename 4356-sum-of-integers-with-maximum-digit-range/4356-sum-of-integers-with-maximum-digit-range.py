class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        def digitrange(a):
            num = [int(d) for d in str(a)]
            maxi = max(num)
            mini = min(num)
            return maxi-mini
        output = []
        for i in range(len(nums)):
            output.append(digitrange(str(nums[i])))
        maxi = max(output)
        ans = []
        for i in range(len(nums)):
            if output[i] == maxi:
                ans.append(nums[i])
        return sum(ans)