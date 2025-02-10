class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = [0, 0, 0]
        l = 0
        result = 0

        for r in range(len(s)):
            count[ord(s[r]) - ord('a')] += 1

            while all(count):
                result += len(s) - r
                count[ord(s[l]) - ord('a')] -= 1
                l += 1

        return result