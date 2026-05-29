class Solution:
    def minElement(self, nums: List[int]) -> int:
        output = []
        for i in nums:
            summ = 0
            while i > 0 :
                summ += i % 10
                i //= 10
            output.append(summ)

        return min(output)