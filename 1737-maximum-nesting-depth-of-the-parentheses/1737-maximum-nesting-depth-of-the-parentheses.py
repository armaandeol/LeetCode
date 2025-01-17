class Solution:
    def maxDepth(self, s: str) -> int:
        output = []
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                output.append(i)
            elif s[i] == ')':
                ans = max(ans, len(output))
                output.pop()
        return ans