class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        s = s.split(' ')
        for i in range(len(s)):
            if s[-1-i] != '':
                ans.append(s[-1-i])
        return ' '.join(ans)