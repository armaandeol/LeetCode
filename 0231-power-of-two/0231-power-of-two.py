class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        take = -1
        while 2 ** take < n:
            take += 1
        return 2 ** take == n
        