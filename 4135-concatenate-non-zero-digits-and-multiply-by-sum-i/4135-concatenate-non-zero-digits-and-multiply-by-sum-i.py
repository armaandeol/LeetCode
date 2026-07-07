class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        a = [int(i) for i in str(n) if i != '0']
        summ = sum(a)
        ans = int(''.join(map(str, a)))
        return ans * summ