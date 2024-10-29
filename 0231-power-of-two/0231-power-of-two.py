class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        number = 0
        while 2 ** number < n:
            number += 1
        return 2 ** number == n
        