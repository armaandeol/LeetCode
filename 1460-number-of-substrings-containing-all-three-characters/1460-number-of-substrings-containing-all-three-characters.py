class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = [0, 0, 0]
        l = 0
        result = 0

        for r in range(len(s)):
            res[ord(s[r]) - ord('a')] += 1

            while all(res):
                result += len(s) - r
                res[ord(s[l]) - ord('a')] -= 1
                l += 1

        return result