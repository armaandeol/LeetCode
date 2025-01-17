class Solution:
    def maxDepth(self, s: str) -> int:
        output,ans = 0,0
        for i in range(len(s)):
            if s[i] == '(':
                output += 1
            elif s[i] == ')':
                ans = max(ans, output)
                output -= 1
            output = max(output, 0)
        return ans