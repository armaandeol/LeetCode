class Solution:
    def isPalindrome(self, x: int) -> bool:
        revNum = 0
        dup = x
        while x > 0:
            digit = x%10
            revNum *= 10
            revNum += digit

            x = x // 10

        return dup == revNum
        