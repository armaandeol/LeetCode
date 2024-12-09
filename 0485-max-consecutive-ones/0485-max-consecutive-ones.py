class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        a = 0
        for i in nums:
            if i == 1:
                maxx += 1
            else :
                a = max(maxx, a)
                maxx = 0

        a = max(maxx, a)
        return a
        